from datetime import timedelta

from django.db.models import Sum
from django.utils.datetime_safe import date

from analytics.models import Entry
from sprints.models import Sprint
from tasks.models import Task


def get_sum(sprint: Sprint) -> float:
    """
    Computes the sum of work hours for a sprint

    """
    total = 0
    return total


def get_sprint_data(sprint: Sprint) -> tuple[list, list]:
    """
    Computes and returns daily work hours data for a sprint

    """
    # get sprint date range
    start_date = sprint.start_date
    end_date = sprint.end_date

    # initialise values
    day_range = get_day_range(start_date, end_date)
    hours = []

    # operation
    for day in day_range:
        entries = Entry.objects.filter(date=day)
        duration = 0

        if entries.count() > 0:
            agg = entries.aggregate(total=Sum('duration'))
            duration = agg['total']
            duration = int(duration.days * 24)

        hours.append(duration)

    return day_range, hours


def get_day_range(start: date, end: date, step_size=1) -> list[date]:
    """
    Returns the dates within the specified range inclusive

    """
    delta = end - start
    day_range = []

    for day in range(delta.days + step_size):
        td = start + timedelta(days=day)
        day_range.append(td)

    return day_range

def get_member_analytics(member):
    sprints = []
    entries = []
    total = 0

    all_tasks_by_member = Task.objects.filter(assignee=member)
    for sprint in Sprint.objects.all():
        total = 0
        for task in sprint.tasks.filter(assignee=member):
            sprints.append(sprint)
            entries.append(Entry.objects.filter(task=task))

    return entries, sprints
