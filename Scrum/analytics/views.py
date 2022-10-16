from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from sprints.models import Sprint
from .forms import EntryForm
from .models import Entry
from .utils import get_sprint_data


class RecentEntryView(ListView):
    model = Entry
    ordering = ['-timestamp']
    paginate_by = 10


class AddEntryView(CreateView):
    model = Entry
    form_class = EntryForm

    def get_success_url(self):
        pk = self.object.task.sprint.pk
        success_url = reverse_lazy('sprint-detail', kwargs={'pk': pk})
        return success_url


class DailyTeamAnalytics(ListView):

    ordering = ['-status']
    template_name = 'analytics/analytics.html'
    context_object_name = 'sprint_list'
    queryset = Sprint.objects.filter(Q(status=Sprint.ONGOING))
    # Q(status=Sprint.ONGOING) | Q(status=Sprint.ENDED))

    def get_context_data(self, **kwargs):
        context = super(DailyTeamAnalytics, self).get_context_data(**kwargs)

        context['x_data'] = {}
        context['y_data'] = {}
        context['sum'] = {}
        context['avg'] = {}

        print(self.context_object_name)

        for q in self.queryset.all():
            chart_data = get_sprint_data(q)
            context['x_data'][q] = chart_data[0]    # dates
            context['y_data'][q] = chart_data[1]    # hours

        return context
