from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Members


def index(request):

    members = Members.objects.all().values()
    context = {
        'members': members,
    }

    return render(request, 'members/index.html', context)

def add(request):
    return render(request, 'members/add.html')

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(first_name=x, last_name=y)
  member.save()

  return HttpResponseRedirect(reverse('index'))
