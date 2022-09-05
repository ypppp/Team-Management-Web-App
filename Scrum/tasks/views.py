from django.shortcuts import render
from .models import Task
from django.views.generic import (DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  ListView)

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task

class TaskUpdateView(UpdateView):
    model = Task

class TaskDeleteView(DeleteView):
    model = Task

class TaskListView(ListView):
    model = Task