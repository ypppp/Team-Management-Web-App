from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .models import Member


class MemberListView(ListView):
    model = Member


class MemberDetailView(DetailView):
    model = Member

    # def get_data(self):
    #     result = {}
    #
    #     result[' '] = 1
    #
    #     return result
    #
    # def get_context_data(self, **kwargs):
    #     context = super(MemberDetailView, self).get_context_data(**kwargs)
    #     context['data'] = self.get_data()
    #     return context


class MemberCreateView(CreateView):
    model = Member
    success_url = reverse_lazy('member-list')


class MemberUpdateView(UpdateView):
    model = Member
    success_url = reverse_lazy('member-list')


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('member-list')
