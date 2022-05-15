from django import template

register = template.Library()

@register.filter('mulInt')
def mulInt(input, argument):
    output = int(input) * argument
    return output

@register.filter('roundOff')
def roundOff(input):
    return int(input)
