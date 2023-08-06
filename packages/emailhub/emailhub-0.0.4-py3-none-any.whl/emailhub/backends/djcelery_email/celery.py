# -*- coding: utf-8 -*-
"""
EmailHub djcelery_email Celery backend
"""

from djcelery_email.backends import CeleryEmailBackend # noqa pylint: disable=import-error
from emailhub.utils.email import process_outgoing_email


class EmailBackend(CeleryEmailBackend):
    """ Celery email backend """
    def send_messages(self, email_messages):  # noqa pylint: disable=missing-docstring
        for message in email_messages:
            process_outgoing_email(message)
        super(EmailBackend, self).send_messages(email_messages)
