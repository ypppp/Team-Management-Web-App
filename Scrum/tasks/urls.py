from django.urls import path
from . import views
from .views import (TaskListView, TaskDetailView, TaskDeleteView, testing1, TaskListViewSortBySprint)


urlpatterns = [
    path('', views.home, name='dashboard'),
    path('productbacklog/', TaskListView.as_view(), name='product-backlog'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('testing/', testing1, name='testis'),
    path('productbacklog/sortbysprint/', TaskListViewSortBySprint.as_view(), name='product-backlog-sort-by-sprint'),
]