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
    "Subtracts the arg from the value"
    return value.tasks.filter(status=Task.COMPLETE).count()


register.filter('percentage', percentage)
register.filter('filter_by_complete', filter_by_complete)
