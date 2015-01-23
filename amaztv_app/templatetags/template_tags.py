from django import template

register = template.Library()

@register.filter(name='no_single_quote')
def no_single_quote(string):
    return string.replace("'", '"')