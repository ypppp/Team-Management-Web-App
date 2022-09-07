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


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('product-backlog')


class TaskListViewSortBySprint(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-sprint']


class TaskListViewSortByAssignee(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-assignee']


class TaskListViewSortByStatus(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-status']


class TaskListViewSortByPriority(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-priority']