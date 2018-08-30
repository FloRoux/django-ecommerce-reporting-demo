from django import template

register = template.Library()

@register.filter(name='mult')
def mult(value, arg):
    return value*arg
