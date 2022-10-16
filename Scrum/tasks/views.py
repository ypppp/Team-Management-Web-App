from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from sprints.models import Sprint
from .forms import TaskForm
from .models import Task


def home(request):
    context = {
        'title': 'Dashboard',
        'content': 'Welcome to the home page!'
    }
    return render(request, 'tasks/dashboard.html', context)

def filterView(request):
    title = request.GET.get('title_contains')
    print("=============")
    print(title)
    return render(request, 'tasks/task_list.html', {'title': title})

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


# sorting functions
class TaskListViewSortBySprintAscending(ListView):
    model = Task
    ordering = ['sprint']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortByAssigneeAscending(ListView):
    model = Task
    ordering = ['assignee']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortByStatusAscending(ListView):
    model = Task
    ordering = ['status']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortByPriorityAscending(ListView):
    model = Task
    ordering = ['priority']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortByDeadlineAscending(ListView):
    model = Task
    ordering = ['due_date']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortBySprintDescending(ListView):
    model = Task
    ordering = ['-sprint']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortByAssigneeDescending(ListView):
    model = Task
    ordering = ['-assignee']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortByStatusDescending(ListView):
    model = Task
    ordering = ['-status']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortByPriorityDescending(ListView):
    model = Task
    ordering = ['-priority']
    paginate_by = 10
    paginate_orphans = 2


class TaskListViewSortByDeadlineDescending(ListView):
    model = Task
    ordering = ['-due_date']

class DashboardList(ListView):
    model = Sprint
    template_name = "tasks/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardList, self).get_context_data(**kwargs)
        context['PENDING'] = Sprint.PENDING
        context['ONGOING'] = Sprint.ONGOING
        context['ENDED'] = Sprint.ENDED
        context['sprint_ongoing'] = Sprint.objects.all().filter(status=Sprint.ONGOING)
        context['sprint_ended'] = Sprint.objects.all().filter(status=Sprint.ENDED)
        context['sprint_pending'] = Sprint.objects.all().filter(status=Sprint.PENDING)
        context['sprint_all'] = Sprint.objects.all()
        context['TASK_PENDING'] = Task.PENDING
        context['TASK_IN_PROGRESS'] = Task.IN_PROGRESS
        context['TASK_COMPLETE'] = Task.COMPLETE

        return context
