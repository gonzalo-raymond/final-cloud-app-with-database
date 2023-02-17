from django import template

register = template.Library()

@register.simple_tag

def update_variable(value):
    """Allows to update existing variable in template"""
    return value

def switch(value):
    
    return not value