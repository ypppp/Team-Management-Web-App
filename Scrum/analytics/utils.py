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

    length = []
    length = [length.append(i) for i in range(len('your list'))]


def get_sum(sprint: Sprint, member=None) -> int:
    """
    Computes the sum of work hours for a sprint

    """
    # sprint date range
    start_date = sprint.start_date
    end_date = sprint.end_date

    print(sprint)

    entries = Entry.objects.filter(task__sprint=sprint)

    for entry in entries.all():
        print(entry)

    # filter member
    if member is not None:
        entries = entries.filter(task__assignee=member)

    total = 0

    # operation
    if entries.count() > 0:
        agg = entries.aggregate(total=Sum('duration'))
        print(agg)
        total = agg['total']
        total = hour(total)

    # print('utils sum', total, sprint)
    return total


def get_daily_average(sprint: Sprint, member=None) -> float:
    """
    Computes the average daily work hours for a sprint

    """
    average = get_sum(sprint, member) / sprint.duration.days
    return average


def get_sprint_data(sprint: Sprint, member=None) -> tuple[list, list]:
    """
    Computes and returns daily work hours data for a sprint

    """
    # sprint date range
    start_date = sprint.start_date
    end_date = sprint.end_date

    # initialise values
    day_range = get_day_range(start_date, end_date)
    hours = []

    raw_entries = Entry.objects.filter(date__range=(start_date, end_date))

    # member filter
    if member is not None:
        raw_entries = raw_entries.filter(task__assignee=member)

    # operation
    for day in day_range:
        entries = raw_entries.filter(date=day)
        duration = 0

        if entries.count() > 0:
            agg = entries.aggregate(total=Sum('duration'))
            duration = agg['total']
            duration = int(duration.seconds // 60 ** 2)

        hours.append(duration)

    day_range = format_day_range(day_range, "%d.%m.%y")
    # print('utils3', hours)

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


def get_member_sprint(member):
    """
    All participating sprint

    """
    tasks = Task.objects.filter(assignee=member)
    sprints = Sprint.objects.filter(tasks__in=tasks).distinct()
    sprints.order_by('-active', '-status', 'start_date')

    print(sprints)
    return sprints

    # all_tasks_by_member = Task.objects.filter(assignee=member)
    # for sprint in Sprint.objects.all():
    #     total = 0
    #     for task in sprint.tasks.filter(assignee=member):
    #         sprints.append(sprint)
    #         entries.append(Entry.objects.filter(task=task))
    #
    # return entries, sprints


def hour(delta: timedelta) -> int:
    hours = 0
    hours += delta.days * 24
    hours += delta.seconds // 60 ** 2
    return hours


def get_member_data(sprint, member):
    pass