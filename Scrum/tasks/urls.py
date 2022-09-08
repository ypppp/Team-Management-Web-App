from django.urls import path
from . import views
from .views import (TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView, TaskListViewSortBySprintAscending, TaskListViewSortByAssigneeAscending, TaskListViewSortByStatusAscending, TaskListViewSortByPriorityAscending)


urlpatterns = [
    path('', views.home, name='dashboard'),
    path('productbacklog/', TaskListView.as_view(), name='product-backlog'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('productbacklog/sortbysprint/ascending', TaskListViewSortBySprintAscending.as_view(), name='sort-by-sprint-ascending'),
    path('productbacklog/sortbyassignee/ascending', TaskListViewSortByAssigneeAscending.as_view(), name='sort-by-assignee-ascending'),
    path('productbacklog/sortbystatus/ascending', TaskListViewSortByStatusAscending.as_view(), name='sort-by-status-ascending'),
    path('productbacklog/sortbypriority/ascending', TaskListViewSortByPriorityAscending.as_view(), name='sort-by-priority-ascending'),

    path('productbacklog/sortbysprint/descending', views.TaskListViewSortBySprintDescending.as_view(), name='sort-by-sprint-descending'),
    path('productbacklog/sortbyassignee/descending', views.TaskListViewSortByAssigneeDescending.as_view(), name='sort-by-assignee-descending'),
    path('productbacklog/sortbystatus/descending', views.TaskListViewSortByStatusDescending.as_view(), name='sort-by-status-descending'),
    path('productbacklog/sortbypriority/descending', views.TaskListViewSortByPriorityDescending.as_view(), name='sort-by-priority-descending'),

]