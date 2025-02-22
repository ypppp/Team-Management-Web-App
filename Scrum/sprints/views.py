from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse_lazy, reverse
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
    ordering = ['-active', '-status', 'start_date']

    def get_context_data(self, **kwargs):
        context = super(SprintListView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['PENDING'] = Sprint.PENDING
        context['ONGOING'] = Sprint.ONGOING
        context['ENDED'] = Sprint.ENDED
        return context


class SprintDetailView(DetailView):
    model = Sprint

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        context['all_start_sprint'] = Sprint.objects.filter(status=Sprint.ONGOING).count
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
    return redirect('sprint-detail', pk)


class SprintStartEndView(DetailView):
    model = Sprint
    template_name = "sprints/sprint_confirm_save.html"

    def get_context_data(self, **kwargs):
        context = super(SprintStartEndView, self).get_context_data(**kwargs)
        # context['incomplete_tasks'] = Task.objects.all().filter(sprint=self.object, status="IN").count
        context['incomplete_tasks'] = self.object.tasks.filter(status=Task.IN_PROGRESS).count
        context['pending_tasks'] = Task.objects.all().filter(sprint=self.object, status="CM").count
        context['PENDING'] = Sprint.PENDING
        context['ONGOING'] = Sprint.ONGOING
        context['ENDED'] = Sprint.ENDED
        return context

