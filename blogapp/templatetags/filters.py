from django import template

register = template.Library()

def cut(value, arg):

    return value.lower()
register.filter('cut', cut)