from django import template
import random

register = template.Library()

@register.filter(name='discount')
def discount(value):
    return int(value*(1+(random.randint(1,20)/100)))

@register.filter(name='miles_to_km')
def miles_to_km(value):
    return int(value*1.6)
