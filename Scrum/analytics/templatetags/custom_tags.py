from django import template


register = template.Library()

@register.filter
def get_obj_field(obj, key):
    return obj[key]