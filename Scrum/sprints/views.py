from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.template import loader
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from sprints.forms import SprintForm
from tasks.models import Task
from sprints.models import Sprint


class SprintCreateView(CreateView):
    model = Sprint
    form_class = SprintForm

    # def get_success_url(self):
    #     success_url = reverse_lazy('sprint-detail', kwargs={'pk': self.object.pk})
    #     return success_url

class SprintUpdateView(UpdateView):
    model = Sprint
    form_class = SprintForm

    def get_success_url(self):
        print('Fuck this shit')
        print(self.object)
        success_url = reverse_lazy('sprint-detail', kwargs={'pk': self.object.pk})
        return success_url


class SprintDeleteView(DeleteView):
    model = Sprint
    success_url = reverse_lazy('sprint-backlog')


class SprintListView(ListView):
    model = Sprint
    template_name = 'sprints/sprint_backlog.html'


class SprintDetailView(DetailView):
    model = Sprint
    # context_object_name = 'sprint'
    # template_name = 'sprints/sprint_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(SprintDetailView, self).get_context_data(**kwargs)
    #     context['tasks'] = Task.objects.all().order_by('status')
    #     return context


def toggle_start_end(request, id):

    sprint = Sprint.objects.get(id=id)
    all_task = Task.objects.all().filter(sprint=sprint)

    if sprint.status == Sprint.PENDING:
        sprint.status = Sprint.ONGOING

    elif sprint.status == Sprint.ONGOING:
        sprint.status = Sprint.ENDED
        for task in all_task:
            if task.sprint is not None and task.status != Task.COMPLETE:
                task.sprint = None
                task.status = Task.OVERDUE
                task.save()

    sprint.save()
    template = loader.get_template('sprints/sprint_confirm_save.html')
    context = {
        'sprint': sprint,
    }
    return HttpResponse(template.render(context, request))



