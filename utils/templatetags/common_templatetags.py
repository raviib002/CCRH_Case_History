from django import template
import urllib.parse
register = template.Library()
from urllib.parse import urlencode
import os
from django.conf import settings



@register.filter(is_safe=True)
def convert_to_int(value):
    try:
        if value:
            return int(value)
    except:
        return None
"""Convert other datatypes to Integer - ends"""

"""To get the file name - starts """
@register.filter(is_safe=True)
def get_filename(value):
    try:
        return os.path.basename(value.file.name)
    except:
        return ''
    
# Get settings value in template
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")
