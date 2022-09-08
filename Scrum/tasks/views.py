from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader

from .models import Task
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)


def home(request):
    context = {
        'title': 'Dashboard',
        'content': 'Welcome to the Scrum home page!'
    }
    return render(request, 'tasks/dashboard.html', context)


# display table function
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date']


class TaskUpdateView(UpdateView):
    model = Task


# delete function
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('product-backlog')


# sorting functions
class TaskListViewSortBySprintAscending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['sprint']


class TaskListViewSortByAssigneeAscending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['assignee']


class TaskListViewSortByStatusAscending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['status']


class TaskListViewSortByPriorityAscending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['priority']


class TaskListViewSortBySprintDescending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-sprint']


class TaskListViewSortByAssigneeDescending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-assignee']


class TaskListViewSortByStatusDescending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-status']


class TaskListViewSortByPriorityDescending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-priority']


