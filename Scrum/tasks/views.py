from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .forms import TaskForm
from .models import Task


def home(request):
    context = {
        'title': 'Dashboard',
        'content': 'Welcome to the home page!'
    }
    return render(request, 'tasks/dashboard.html', context)


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    paginate_by = 20


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('product-backlog')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('product-backlog')


class TaskStatusUpdate(UpdateView):
    model = Task
    fields = ['status']
    success_url = reverse_lazy('sprint-backlog')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('product-backlog')


# sorting functions
class TaskListViewSortBySprintAscending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['sprint']


class TaskListViewSortByAssigneeAscending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['assignee']


class TaskListViewSortByStatusAscending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['status']


class TaskListViewSortByPriorityAscending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['priority']


class TaskListViewSortByDeadlineAscending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['due_date']


class TaskListViewSortBySprintDescending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['-sprint']


class TaskListViewSortByAssigneeDescending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['-assignee']


class TaskListViewSortByStatusDescending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['-status']


class TaskListViewSortByPriorityDescending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['-priority']


class TaskListViewSortByDeadlineDescending(ListView):
    model = Task
    template_name = 'tasks/product_backlog.html'
    ordering = ['-due_date']
