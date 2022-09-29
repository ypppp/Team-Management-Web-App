from django.urls import path
from .views import SprintCreateView

urlpatterns = [
    path('', SprintCreateView.as_view(), name='sprint_create_form'),
]
