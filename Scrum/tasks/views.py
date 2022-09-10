from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.template import loader

from .forms import TaskForm
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


class FormActionMixin(object):

    def post(self, request, *args, **kwargs):
        """Add 'Cancel' button redirect."""
        if "cancel" in request.POST:
            url = reverse('product-backlog')
            return HttpResponseRedirect(url)
        else:
            return super(FormActionMixin, self).post(request, *args, **kwargs)


class TaskCreateView(CreateView, FormActionMixin):
    model = Task
    form_class = TaskForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('product-backlog')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('product-backlog')


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


class TaskListViewSortByDeadlineAscending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['due_date']


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


class TaskListViewSortByDeadlineDescending(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-due_date']
