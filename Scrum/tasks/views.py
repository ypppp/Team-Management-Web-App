from django.shortcuts import render
from .models import Task
from django.views.generic import (DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task

class TaskUpdateView(UpdateView):
    model = Task

class TaskDeleteView(DeleteView):
    model = Task
