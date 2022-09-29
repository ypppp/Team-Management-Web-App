from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader
from tasks import models, forms
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from tasks.models import Task


# START OF <SPRINT LIST>

# for sprintlist before and after start, shows all the details of sprint including the 2 tables
class SprintListView(ListView):
    model = Sprint  # models
    context_object_name = 'sprints'
    template_name = 'sprints/sprint_list_1.html'
# path('sprint/<int:pk>/', SprintListView.as_view(), name='sprint_list_before_start'


# for sprintlist after start, edit the status in the table
class SprintListUpdateView(UpdateView):
    model = Sprint
    fields = [
        "status"
    ]
    reverse_lazy('sprint-list-after-start')
# path('task/<int:pk>/', SprintListUpdateView.as_view(), name='sprint-list-update'),

class SprintBacklogView(ListView):
    model = Sprint
    context_object_name = 'sprints'
    template_name = 'sprints/sprint_backlog.html'

