from datetime import timedelta, date

from django.db.models import Q, Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.list import MultipleObjectMixin

from sprints.models import Sprint
from .forms import EntryForm
from .models import Entry


class RecentEntryView(ListView):
    model = Entry
    paginate_by = 10


class AddEntryView(CreateView):
    model = Entry
    form_class = EntryForm

    def get_success_url(self):
        pk = self.object.task.sprint.pk
        success_url = reverse_lazy('sprint-detail', kwargs={'pk': pk})
        return success_url


class EntriesMixin(MultipleObjectMixin):
    # queryset = Task.objects.entries
    pass


def get_sum(sprint):
    duration_sum = timedelta(hours=0)
    for task in sprint.tasks.all():
        for entry in task.entries.all():
            duration_sum += entry.duration
    return {'sum': duration_sum}


def get_sprint_data(sprint: Sprint) -> list:
    """
        Computes and returns statistical data for a sprint
    Args:
        sprint: Target sprint

    Returns:
        List of dictionary containing chart data where:
            - x is date
            - y is hours
    """
    # get sprint date range
    start_date = sprint.start_date
    end_date = sprint.end_date

    delta = end_date - start_date
    day_range = [end_date]

    for day in range(delta.days):
        day_range.insert(-1, start_date + timedelta(days=day))

    # initialise values
    entries = Entry.objects.filter(task__sprint=sprint)
    print(entries)

    # data = {'chart_data': []}
    chart_data = []
    total = timedelta()

    # operation
    for day in day_range:

        target = entries.filter(date=day)
        hours = 0

        if target.count() > 0:
            duration = target.aggregate(duration=Sum('duration'))
            # print(duration, 'hours')
            hours = int(duration['duration'].days) * 24

        chart_data.append({'date': day, 'hours': hours})
        # total += hours

    # data['sum'] = total
    # data['avg'] = hours / len(day_range)
    # print(chart_data)
    return chart_data


class DailyTeamAnalytics(ListView):
    """
        - all tasks in a sprint combined?
        - how to design date range?
        - what stat value to include?
        - all the sprints?
        - all the sprints combined? (composite)
    """
    queryset = Sprint.objects.filter(Q(status=Sprint.ONGOING)).order_by('-status')
    # queryset = Sprint.objects.exclude(Q(status=Sprint.PENDING))
    template_name = 'analytics/analytics.html'

    # def get_chart_data(self):
    #
    #     start_date = self.object.start_date
    #     end_date = self.object.end_date
    #     date = start_date
    #
    #     while date <= end_date:
    #         for entry in task.entries.all():
    #             result += entry.duration
    #
    #         date += timedelta(days=1)
    #
    #     return result

    def get_context_data(self, **kwargs):
        context = super(DailyTeamAnalytics, self).get_context_data(**kwargs)
        a = {'chart_data': [{'date': date(2022, 12, 29), 'hours': 1}, {'date': date(2022, 12, 30), 'hours': 2}, {'date': date(2022, 12, 31), 'hours': 3}], 'sum': 2, 'avg': 3}
        context['date'] = a.get("chart_data")[0]['date']

        # context['data'] = {}
        for q in self.queryset.all():
            chart_data = get_sprint_data(q)
            hours, dates, data = get_data_list(chart_data)
            context['hour'] = hours
            context['date'] = dates
            context['date_data'] = data

        return context

def get_data_dic(dic):
    hours = []
    date = []
    length = len(dic.get("chart_data"))

    for i in range(length):
        hours.append(dic.get("chart_data")[i]['hours'])
        date.append(dic.get("chart_data")[i]['date'])

    return hours, date

def get_data_list(list):
    hours = []
    date = []
    date_data = []

    for i in range(len(list)):
        hours.append(list[i]["hours"])
        date.append(list[i]["date"].strftime("%d.%m.%y"))
        date_data.append(i+1)

    return hours, date, date_data
