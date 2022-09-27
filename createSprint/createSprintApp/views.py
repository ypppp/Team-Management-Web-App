from django.shortcuts import render
from .forms import SprintForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    form = SprintForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Sprint created successfully!")
        return HttpResponseRedirect('/')
    context = {
        "form": form
    }
    return render(request, 'sprint_create_form.html', context)
