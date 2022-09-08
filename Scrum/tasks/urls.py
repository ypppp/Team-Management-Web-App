from django.urls import path
from . import views
from .views import (TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView, TaskListViewSortBySprintAscending, TaskListViewSortByAssigneeAscending, TaskListViewSortByStatusAscending, TaskListViewSortByPriorityAscending)


urlpatterns = [
    path('', views.home, name='dashboard'),
    path('productbacklog/', TaskListView.as_view(), name='product-backlog'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/', views.TaskUpdateView.as_view(), name='task-form'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    path('productbacklog/sortby/sprint/ascending', TaskListViewSortBySprintAscending.as_view(), name='sort-by-sprint-ascending'),
    path('productbacklog/sortby/assignee/ascending', TaskListViewSortByAssigneeAscending.as_view(), name='sort-by-assignee-ascending'),
    path('productbacklog/sortby/status/ascending', TaskListViewSortByStatusAscending.as_view(), name='sort-by-status-ascending'),
    path('productbacklog/sortby/priority/ascending', TaskListViewSortByPriorityAscending.as_view(), name='sort-by-priority-ascending'),

    path('productbacklog/sortby/sprint/descending', views.TaskListViewSortBySprintDescending.as_view(), name='sort-by-sprint-descending'),
    path('productbacklog/sortby/assignee/descending', views.TaskListViewSortByAssigneeDescending.as_view(), name='sort-by-assignee-descending'),
    path('productbacklog/sortby/status/descending', views.TaskListViewSortByStatusDescending.as_view(), name='sort-by-status-descending'),
    path('productbacklog/sortby/priority/descending', views.TaskListViewSortByPriorityDescending.as_view(), name='sort-by-priority-descending'),
]