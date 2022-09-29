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

# for sprintlist before and after start
class SprintListView(DetailView):
    model = Sprint          # models
    context_object_name = 'sprints'

# path('sprint/<pk>/', SprintListView.as_view(), name='sprint_list_before_start'

# for sprintlist after start, edit the status
class SprintListUpdateView(UpdateView):
    model =