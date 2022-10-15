from datetime import timedelta

from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView)
from django.views.generic.list import MultipleObjectMixin

from sprints.models import Sprint
from tasks.models import Task
from .forms import EntryForm
from .models import Entry


class RecentEntryView(ListView):
    model = Entry


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


class TeamAnalytics(DetailView):
    model = Sprint
    template_name = 'analytics/team_stat.html'

    def get_chart_data(self):

        start_date = self.object.start_date

        # for task in raw_entries:
        #     for entry in task.entries.all():
        #         result += entry.duration
        #
        # return result

    def get_sum(self):

        raw_entries = self.object.tasks.all()
        total = timedelta(hours=0)

        for task in raw_entries:
            for entry in task.entries.all():
                print(type(entry.duration))
                total += entry.duration

        return total

    def get_context_data(self, **kwargs):
        context = super(TeamAnalytics, self).get_context_data(**kwargs)
        # context['chart_data'] =
        context['sum'] = self.get_sum()
        return context
