from django.urls import path
from .views import TestListView

urlpatterns = [
    path('sprintlist/', TestListView.as_view(), name='sprint-list'),
    ]
