from django import template


register = template.Library()

@register.filter
def get_dict_value(obj, key):
    return obj[key]

register.filter('get_dict_value', get_dict_value)