from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sprint_create_form'),
]
