from django import template

from tasks.models import Task

register = template.Library()

@register.simple_tag
def percentage(value):
    if value.tasks.filter(status=Task.COMPLETE).count() == 0 or value.tasks.count() == 0:
        return 0
    return int(round((value.tasks.filter(status=Task.COMPLETE).count() / value.tasks.count())*100,2))

@register.simple_tag
def filter_by_complete(value):
    return value.tasks.filter(status=Task.COMPLETE).count()

@register.filter
def filter_count_sprint(value, sprint):
    return value.filter(sprint=sprint).count()

@register.filter
def timedelta_hours(delta):
    hours = 0
    hours += delta.days * 24
    hours += delta.seconds // 60 ** 2
    return hours

@register.filter
def get_dict_value(obj, key):
    return obj[key]


register.filter('get_dict_value', get_dict_value)
register.filter('percentage', percentage)
register.filter('filter_by_complete', filter_by_complete)
register.filter('filter_count_sprint', filter_count_sprint)
register.filter('timedelta_hours', timedelta_hours)
