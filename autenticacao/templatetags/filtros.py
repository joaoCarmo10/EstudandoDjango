from django import template

register = template.Library()

@register.filter(name='teste')
def teste(v1):
    return f"seu valor {id}"