from django.shortcuts import render
from django.views.generic import DetailView
from .models import Sprint


class SprintDetailView(DetailView):
    model = Sprint
