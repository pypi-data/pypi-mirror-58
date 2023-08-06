# -*- coding: utf-8 -*-
"""
EmailHub template tags
"""

from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter
def get_previous_for(message, user):
    """
    Returns previous EmailMessage by date for a given user
    """
    try:
        return message.get_previous_by_date_created(recipients__users=user)
    except ObjectDoesNotExist:
        return None


@register.filter
def get_next_for(message, user):
    """
    Returns next EmailMessage by date for a given user
    """
    try:
        return message.get_next_by_date_created(recipients__users=user)
    except ObjectDoesNotExist:
        return None
