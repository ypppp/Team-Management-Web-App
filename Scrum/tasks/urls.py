from django.urls import path
from . import views
from .views import (TaskListView, TaskDetailView, TaskCreateView, TaskListViewSortBySprint, TaskDeleteView, TaskListViewSortByAssignee, TaskListViewSortByStatus, TaskListViewSortByPriority)


urlpatterns = [
    path('', views.home, name='dashboard'),
    path('productbacklog/', TaskListView.as_view(), name='product-backlog'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('productbacklog/sortbysprint/', TaskListViewSortBySprint.as_view(), name='sort-by-sprint'),
    path('productbacklog/sortbyassignee', TaskListViewSortByAssignee.as_view(),name='sort-by-assignee'),
    path('productbacklog/sortbystatus', TaskListViewSortByStatus.as_view(), name='sort-by-status'),
    path('productbacklog/sortbypriority', TaskListViewSortByPriority.as_view(), name='sort-by-priority'),

]