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
    template_name_suffix = '_create_form'
    form_class = SprintForm

class SprintUpdateView(UpdateView):
    model = Sprint
    form_class = SprintForm

class SprintDeleteView(DeleteView):
    model = Sprint


# START OF <SPRINT LIST>

# for sprint list before and after start, shows all the details of sprint including the 2 tables
class SprintDetailView(DetailView):
    model = Sprint  # models
    context_object_name = 'sprints'
    template_name = 'sprints/sprint_list_1.html'

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        context['task'] = Task.objects.all()
        return context
# path('sprint/<int:pk>/', SprintListView.as_view(), name='sprint_list_before_start'


# for sprint list after start, edit the status in the table
class SprintListUpdateView(UpdateView):
    model = Sprint
    fields = [
        "status"
    ]
    reverse_lazy('sprint-list-after-start')
# path('task/<int:pk>/', SprintListUpdateView.as_view(), name='sprint-list-update'),

# for the button to start
def toggle_start(request):
    sprint = get_object_or_404(Sprint, pk=request.GET.get('sprint_id'))
    sprint.status = "Ongoing"
    sprint.save()
    reverse_lazy('sprint-backlog')

