from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .forms import TaskForm, EntryForm
from .models import Task, Entry


def home(request):
    context = {
        'title': 'Dashboard',
        'content': 'Welcome to the home page!'
    }
    return render(request, 'tasks/dashboard.html', context)


class TaskListView(ListView):
    model = Task
    paginate_by = 10
    paginate_orphans = 2


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class TaskStatusUpdate(UpdateView):
    model = Task
    fields = ['status']
    template_name = 'tasks/task_status_update.html'
    success_url = reverse_lazy('sprint-list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')


class AddEntryView(CreateView):
    model = Entry
    form_class = EntryForm

    def get_success_url(self):
        pk = self.object.task.sprint.pk
        success_url = reverse_lazy('sprint-detail', kwargs={'pk': pk})
        return success_url


# sorting functions
class TaskListViewSortBySprintAscending(ListView):
    model = Task
    ordering = ['sprint']


class TaskListViewSortByAssigneeAscending(ListView):
    model = Task
    ordering = ['assignee']


class TaskListViewSortByStatusAscending(ListView):
    model = Task
    ordering = ['status']


class TaskListViewSortByPriorityAscending(ListView):
    model = Task
    ordering = ['priority']


class TaskListViewSortByDeadlineAscending(ListView):
    model = Task
    ordering = ['due_date']


class TaskListViewSortBySprintDescending(ListView):
    model = Task
    ordering = ['-sprint']


class TaskListViewSortByAssigneeDescending(ListView):
    model = Task
    ordering = ['-assignee']


class TaskListViewSortByStatusDescending(ListView):
    model = Task
    ordering = ['-status']


class TaskListViewSortByPriorityDescending(ListView):
    model = Task
    ordering = ['-priority']


class TaskListViewSortByDeadlineDescending(ListView):
    model = Task
    ordering = ['-due_date']
