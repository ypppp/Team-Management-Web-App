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
    template_name = 'tasks/task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']


class TaskUpdateView(UpdateView):
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('product-backlog')


def filterViewBySprint():
    result = Task.objects.all().order_by('-sprint').values()
    return result


def testing1(request):
    if request.method == "POST":
        data = filterViewBySprint()  # the function you want to call
        template = loader.get_template('tasks/testing.html')
        return HttpResponse(template.render())

class TaskListViewSortBySprint(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/product_backlog.html'
    ordering = ['-sprint']