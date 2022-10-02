from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .models import Member


class MemberListView(ListView):
    model = Member


class MemberDetailView(DetailView):
    model = Member


class MemberCreateView(CreateView):
    model = Member
    success_url = reverse_lazy('product-backlog')


class MemberUpdateView(UpdateView):
    model = Member
    success_url = reverse_lazy('product-backlog')


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('product-backlog')
