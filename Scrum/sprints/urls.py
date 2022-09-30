from django.urls import path
from .views import SprintDetailView


urlpatterns = [
    path('sprint/<int:pk>/', SprintDetailView.as_view(), name='sprint-detail'),
]