from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from sprints.forms import SprintForm
from sprints.models import Sprint
from tasks.models import Task


class SprintCreateView(CreateView):
    model = Sprint
    form_class = SprintForm

    def get_success_url(self):
        success_url = reverse_lazy('sprint-detail', kwargs={'pk': self.object.pk})
        return success_url

class SprintUpdateView(UpdateView):
    model = Sprint
    form_class = SprintForm

    def get_success_url(self):
        success_url = reverse_lazy('sprint-detail', kwargs={'pk': self.object.pk})
        return success_url


class SprintDeleteView(DeleteView):
    model = Sprint
    success_url = reverse_lazy('sprint-list')


class SprintListView(ListView):
    model = Sprint
    ordering = ['-active', '-status']


class SprintDetailView(DetailView):
    model = Sprint

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        context['PENDING'] = Sprint.PENDING
        context['ONGOING'] = Sprint.ONGOING
        context['ENDED'] = Sprint.ENDED
        return context


def toggle_start_end(request, pk):

    sprint = Sprint.objects.get(id=pk)

    if sprint.status == Sprint.PENDING:
        sprint.status = Sprint.ONGOING
        sprint.active = True

    elif sprint.status == Sprint.ONGOING:
        sprint.status = Sprint.ENDED
        sprint.active = False

        tasks = sprint.tasks.all()
        for task in tasks:
            if task.status != Task.COMPLETE:
                # task.sprint = None
                task.status = Task.OVERDUE
                task.save()

    sprint.save()
    template = loader.get_template('sprints/sprint_confirm_save.html')
    context = {
        'sprint': sprint,
        'PENDING': Sprint.PENDING,
        'ONGOING': Sprint.ONGOING,
        'ENDED': Sprint.ENDED,
    }
    return HttpResponse(template.render(context, request))



