from datetime import timedelta

from django.db.models import Sum
from django.utils.datetime_safe import date

from analytics.models import Entry
from sprints.models import Sprint
from tasks.models import Task


def test(sprint, member):
    start_date = sprint.start_date
    end_date = sprint.end_date

    entries = Entry.objects.filter(date__range=(start_date, end_date))

    entries = entries.filter(task__assignee=member)


def get_sum(sprint: Sprint, member=None) -> float:
    """
    Computes the sum of work hours for a sprint

    """
    # sprint date range
    start_date = sprint.start_date
    end_date = sprint.end_date

    entries = Entry.objects.filter(date__range=(start_date, end_date))

    if member is not None:
        entries = Entry.objects.filter(task__assignee=member)

    agg = entries.aggregate(total=Sum('duration'))

    return agg['total']


def get_average(sprint: Sprint) -> float:
    """
    Computes the average daily work hours for a sprint

    """
    # sprint date range
    start_date = sprint.start_date
    end_date = sprint.end_date

    day_count = end_date - start_date
    average = get_sum(sprint) / day_count.days

    return average


def get_sprint_data(sprint: Sprint) -> tuple[list, list]:
    """
    Computes and returns daily work hours data for a sprint

    """
    # sprint date range
    start_date = sprint.start_date
    end_date = sprint.end_date

    # initialise values
    day_range = get_day_range(start_date, end_date)
    hours = []

    # operation
    for day in day_range:
        entries = Entry.objects.filter(date=day)
        # print(entries)
        duration = 0

        if entries.count() > 0:
            agg = entries.aggregate(total=Sum('duration'))
            # print(agg)
            duration = agg['total']
            # print(duration.seconds)
            duration = int(duration.seconds // 60 ** 2)
            # print(duration)

        hours.append(duration)

    day_range = format_day_range(day_range, "%d.%m.%y")

    # print(hours)
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
        # print(type(td))
        # print(td)

    return day_range


def format_day_range(day_range: list[date], frmt: str) -> list[str]:
    day_range = [day.strftime(frmt) for day in day_range]
    # print(day_range)
    # print(type(day_range[0]))
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
