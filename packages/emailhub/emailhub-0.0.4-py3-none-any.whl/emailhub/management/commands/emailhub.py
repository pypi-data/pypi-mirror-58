# -*- coding: utf-8 -*-
"""
EmailHub management command
"""

from __future__ import unicode_literals

import io
import os
import json
import six

from icdiff import ConsoleDiff

from django.conf import settings
from django.core import management
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

from emailhub.conf import settings as emailhub_settings
from emailhub.utils.email import send_unsent_emails
from emailhub.models import EmailTemplate, EmailMessage

User = get_user_model()
WARN = '\033[1;33m⚠\033[0m'
ERR = '\033[1;91m⚠\033[0m'
ADDED = '\033[1;34m⨁\033[0m'


class Command(BaseCommand):
    """
    EmailHub management command
    """
    help = 'EmailHub management command'
    cd = None
    args = []
    options = {}
    verbosity = 1
    commands = [
        'status', 'create_template', 'list_templates', 'send_test',
        'send', 'dump_all', 'dump', 'diff']

    def add_arguments(self, parser):
        parser.add_argument(
            '--send',
            dest='send',
            action='store_true',
            default=False,
            help='Send unsent emails')
        parser.add_argument(
            '--status',
            dest='status',
            action='store_true',
            default=False,
            help='EmailHub system status')
        parser.add_argument(
            '--create-template',
            dest='create_template',
            action='store_true',
            default=False,
            help='Create a new template')
        parser.add_argument(
            '--list-templates',
            dest='list_templates',
            action='store_true',
            default=False,
            help='List templates')
        parser.add_argument(
            '--send-test',
            dest='send_test',
            action='store',
            help='Send test email')
        parser.add_argument(
            '--dump-all',
            dest='dump_all',
            action='store_true',
            default=False,
            help='Dump all templates')
        parser.add_argument(
            '--dump',
            dest='dump',
            action='store',
            help='Dump specified templates')
        parser.add_argument(
            '--diff',
            dest='diff',
            action='store',
            help='Use a JSON dump file and diff it with in database templates')
        parser.add_argument(
            '--indent',
            dest='indent',
            action='store',
            default=None,
            help='Specify the dump indentation')

    def do_status(self):
        """
        Perform status
        """
        qs = EmailMessage.objects.all()
        unsent = qs.filter(state='pending').count()
        drafts = qs.filter(state='draft').count()
        issent = qs.filter(state='sent').count()
        locked = qs.filter(state='locked').count()
        errors = qs.filter(state='error').count()
        self.stdout.write('\n')
        if drafts:
            self.stdout.write(
                "\t{}\033[1m\033[94m{}\033[0m".format(
                    _('Drafts').ljust(30), drafts))
        else:
            self.stdout.write("\t{}{}".format(_('Drafts').ljust(30), drafts))
        if unsent:
            self.stdout.write(
                "\t{}\033[1m\033[95m{}\033[0m".format(
                    _('Unsent').ljust(30), unsent))
        else:
            self.stdout.write(
                "\t{}\033[1m\033[95m{}\033[0m".format(
                    _('Unsent').ljust(30), unsent))
        if locked:
            self.stdout.write(
                "\t{}\033[1m\033[93m{}\033[0m".format(
                    _('Locked').ljust(30), locked))
        else:
            self.stdout.write("\t{}{}".format(_('Locked').ljust(30), locked))
        if issent:
            self.stdout.write(
                "\t{}\033[1m\033[92m{}\033[0m".format(
                    _('Is sent').ljust(30), issent))
        else:
            self.stdout.write("\t{}{}".format(_('Is sent').ljust(30), issent))
        if errors:
            self.stdout.write("\t{}\033[1m\033[91m{}\033[0m".format(
                _('Errors').ljust(30), errors))
        else:
            self.stdout.write("\t{}{}".format(_('Errors').ljust(30), errors))
        self.stdout.write('\n')

    def do_send(self): # pylint: disable=missing-docstring,no-self-use
        send_unsent_emails()

    def do_send_test(self):
        """
        Perform sending test
        """
        if '@' in self.options.get('send_test'):
            to = self.options.get('send_test')
        else:
            to = User.objects.get(pk=int(self.options.get('send_test'))).email
        send_mail('Test email', 'This is a test.',
                  emailhub_settings.DEFAULT_FROM, [to], fail_silently=False)

    def do_create_template(self):
        """
        Create template
        """
        slug = six.input('{}: '.format(_('Slug')))
        for lang in dict(settings.LANGUAGES).keys():
            subject = '{} ({}): '.format(_('Title'), lang.lower())
            et = EmailTemplate(slug=slug, language=lang, subject=subject)
            et.save()
        self.stdout.write('Created template "{}"'.format(slug))

    def do_list_templates(self): # pylint: disable=missing-docstring
        templates = EmailTemplate.objects.all()
        for slug in set(EmailTemplate.objects.values_list('slug', flat=True)):
            self.stdout.write('\n  \033[1m\033[95m{}\033[0m'.format(slug))
            langs = list(dict(settings.LANGUAGES).keys())
            for tpl in templates.filter(slug=slug):
                langs.remove(tpl.language)
                self.stdout.write(
                    '    - {}) {}'.format(tpl.language.upper(), tpl.subject))
            if langs:
                for lang in langs:
                    self.stdout.write(
                        '    \033[91m- {}) MISSING\033[0m'.format(lang.upper()))
        self.stdout.write('\n')

    def do_dump(self):
        """
        Dump template
        """
        out, buf = list(), io.StringIO()
        indent = int(self.options.get('indent')) \
            if self.options.get('indent') else None
        management.call_command(
            'dumpdata', 'emailhub.emailtemplate',
            verbosity=0, stdout=buf, indent=indent)
        buf.seek(0)
        templates = json.loads(buf.read())
        slugs = self.options.get('dump').split(',')
        for template in templates:
            if template['fields']['slug'] in slugs:
                out.append(template)
        print(json.dumps(out, sort_keys=True, indent=indent))

    def do_dump_all(self):
        """
        Dump all templates
        """
        indent = int(self.options.get('indent')) \
            if self.options.get('indent') else None
        management.call_command(
            'dumpdata', 'emailhub.emailtemplate', verbosity=0, indent=indent)

    def string_diff(self, lines_a, lines_b, prefix=""):
        """
        Perform a side-by-side string diff using icdiff
        """
        out = []
        lines = self.cd.make_table(
            lines_a, lines_b, context=False, numlines=False)
        for line in lines:
            out.append('{}{}'.format(prefix, line))
        return '\n{}'.format(prefix).join(out)

    def bool_diff(self, a, b, prefix=""):
        """
        Performs a side-by-side boolean diff
        """
        out = []
        lines = self.cd.make_table(
            [str(a)], [str(b)], context=False, numlines=False)
        for line in lines:
            out.append('{}{}'.format(prefix, line))
        return '\n{}'.format(prefix).join(out)

    def field_diff(self, fs, db, fieldname):
        """
        Create a diff of two fields values, returns the output as string
        """
        out = []
        if fs['fields'][fieldname] == db['fields'][fieldname]:
            if self.verbosity > 2:
                out.append(
                    '\t - {} \033[1m\033[92mOK\033[0m\n'.format(
                        fieldname.ljust(20)))
        else:
            out.append('\n{} \033[1m\033[33m{}\033[0m'.format(WARN, fieldname))
            if self.verbosity > 1:
                _in = '\033[1;30min\033[0m \033[1mDB\033[0m'
                _vs = '\033[1;30mvs\033[0m'
                out.append(' {} {} \033[1m{}\033[0m'.format(
                    _in, _vs, self.options.get('diff')))
                if fieldname in ['is_active', 'is_auto_send']:
                    _diff = self.bool_diff
                    A = db['fields'][fieldname]
                    B = fs['fields'][fieldname]
                else:
                    _diff = self.string_diff
                    if db['fields'][fieldname]:
                        A = db['fields'][fieldname].split('\n')
                    else:
                        A = ['null']
                    if fs['fields'][fieldname]:
                        B = fs['fields'][fieldname].split('\n')
                    else:
                        B = ['null']
                rs = _diff(A, B)
                out.append('\n{}'.format(rs))
        if out:
            return ''.join(out)
        return None

    def diff_from_db(self, indb_templates, onfs_templates):
        """
        Performs a diff of a json file against templates in database
        """
        for db_tpl in indb_templates:
            fs_tpl = None
            for tpl in onfs_templates:
                if tpl['fields']['slug'] == db_tpl['fields']['slug'] and \
                    tpl['fields']['language'] == db_tpl['fields']['language']:
                    fs_tpl = tpl
            if fs_tpl:
                changes = [
                    self.field_diff(fs_tpl, db_tpl, 'subject'),
                    self.field_diff(fs_tpl, db_tpl, 'text_content'),
                    self.field_diff(fs_tpl, db_tpl, 'html_content'),
                    self.field_diff(fs_tpl, db_tpl, 'email_from'),
                    self.field_diff(fs_tpl, db_tpl, 'is_auto_send'),
                    self.field_diff(fs_tpl, db_tpl, 'is_active'),
                ]
                if any(changes):
                    _line = '\n    \033[1;30m[\033[96m{}\033[0m\033[1;30m] '
                    _line += '\033[1m\033[95m{}\033[0m \033[96m{}\033[0m'
                    self.stdout.write(
                        _line.format(
                            db_tpl['pk'],
                            db_tpl['fields']['slug'],
                            db_tpl['fields']['language'].upper()))
                    for change in changes:
                        if change:
                            self.stdout.write(
                                change.replace(
                                    '\\x1b', '\033').replace('\n', '\n\t'))
            else:
                _line = '\n    \033[1;30m[\033[91m?\033[0m\033[1;30m] '
                _line += '\033[1m\033[95m{}\033[0m \033[96m{}\033[0m'
                self.stdout.write(
                    _line.format(
                        db_tpl['fields']['slug'],
                        db_tpl['fields']['language'].upper()))
                self.stdout.write('\n        {} \033[91m{}\033[0m {}'.format(
                    ERR, 'Not found in', self.options.get('diff')))
            fs_tpl = None

    def diff_from_fs(self, indb_templates, onfs_templates):
        """
        Performs a diff of templates in database a json file against
        """
        for tpl in onfs_templates:
            fs_tpl = None
            for db_tpl in indb_templates:
                if tpl['fields']['slug'] == db_tpl['fields']['slug'] and \
                    tpl['fields']['language'] == db_tpl['fields']['language']:
                    fs_tpl = tpl
            if fs_tpl is None:
                _line = '\n    \033[1;30m[\033[34m{}\033[0m\033[1;30m] '
                _line += '\033[1m\033[95m{}\033[0m \033[96m{}\033[0m'
                self.stdout.write(
                    _line.format(
                        tpl['pk'],
                        tpl['fields']['slug'],
                        tpl['fields']['language'].upper()))
                self.stdout.write('\n        {}  \033[1;34m{}\033[0m {}'.format(
                    ADDED, 'Not present in', 'database'))

    def do_diff(self):
        """
        Diff templates
        """
        file_to_diff = self.options.get('diff')

        if not os.path.exists(file_to_diff):
            raise management.CommandError(
                'File does not exists: {}'.format(file_to_diff))

        with open(file_to_diff, 'r') as fd:
            onfs_templates = json.load(fd)
        buf = io.StringIO()

        management.call_command(
            'dumpdata', 'emailhub.emailtemplate', verbosity=0, stdout=buf)
        buf.seek(0)
        indb_templates = json.loads(buf.read())
        self.diff_from_db(indb_templates, onfs_templates)
        self.diff_from_fs(indb_templates, onfs_templates)
        self.stdout.write('\n')

    def handle(self, *args, **opts):
        """
        Dispatch command
        """
        self.args = args
        self.options = opts
        self.verbosity = self.options.get('verbosity', 1)
        self.cd = ConsoleDiff(
            cols=4, show_all_spaces=True, highlight=True, line_numbers=False,
            tabsize=4)

        for command_name in self.commands:
            command = 'do_{}'.format(command_name)
            if self.options.get(command_name) and hasattr(self, command):
                getattr(self, command)()
