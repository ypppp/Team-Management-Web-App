from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader

import sprints.models
from tasks import models, forms
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
import datetime
from tasks.models import Task
from sprints.models import Sprint


# START OF <SPRINT LIST>

class SprintListView(ListView):
    model = Sprint
    context_object_name = 'sprints'
    template_name = 'sprints/sprint_backlog.html'

    def get_context_data(self, **kwargs):
        context = super(SprintListView, self).get_context_data(**kwargs)
        context['timenow'] = datetime.datetime.now()
        return context

