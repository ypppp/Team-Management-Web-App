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

class SprintUpdateView(UpdateView):
    model = Sprint
    form_class = SprintForm

class SprintDeleteView(DeleteView):
    model = Sprint


# START OF <SPRINT LIST>

# for sprintlist before and after start, shows all the details of sprint including the 2 tables
class SprintDetailView(DetailView):
    model = Sprint

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        context['all_start_sprint'] = Sprint.objects.filter(status="ON").count
        context['tasks'] = Task.objects.all().order_by('status')
        pk = self.object.pk
        print("------------------")
        print(pk)
        return context


# for sprintlist after start, edit the status in the table
class SprintListUpdateView(UpdateView):
    model = Sprint
    fields = [
        "status"
    ]
    reverse_lazy('sprint-list-after-start')


# path('task/<int:pk>/', SprintListUpdateView.as_view(), name='sprint-list-update'),

# for the button to start
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


class SprintListView(ListView):
    model = Sprint
    template_name = 'sprints/sprint_backlog.html'


