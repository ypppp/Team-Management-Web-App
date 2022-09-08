from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.views.generic import (ListView, DetailView, FormView,
                                  CreateView, UpdateView, DeleteView)


def home(request):
    context = {
        'title': 'Dashboard',
        'content': 'Welcome to the Scrum home page!'
    }
    return render(request, 'tasks/dashboard.html', context)


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    # ordering = ['sprint', 'priority']


class TaskDetailView(DetailView):
    model = Task


class TaskFormView(FormView):
    model = Task
    form_class = TaskForm
    success_url = '/'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    # fields = ['title', 'description', 'due_date']


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = 'productbacklog/'

