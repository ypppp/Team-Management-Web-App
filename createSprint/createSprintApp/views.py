from django.shortcuts import render
from django.views.generic import CreateView

from .forms import SprintForm

from .models import Sprint


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home.html', context)


class SprintCreateView(CreateView):
    model = Sprint
    form_class = SprintForm
    template_name = 'create_sprint_form.html'
