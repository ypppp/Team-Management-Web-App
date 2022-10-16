from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .forms import MemberForm
from .models import Member
from tasks.models import Task
from sprints.models import Sprint


class MemberListView(ListView):
    model = Member


class MemberDetailView(DetailView):
    model = Member
    template_name = "members/member_detail.html"

    def get_context_data(self, **kwargs):

        def division_zero_avoid(arg1, arg2):
            if arg1 == 0 or arg2 == 0:
                return 0
            return (arg1 / arg2) * 100

        context = super(MemberDetailView, self).get_context_data(**kwargs)
        tasks = Task.objects.all().filter(assignee=self.object)
        context["tasks_involved"] = tasks.count()
        context["tasks_done"] = division_zero_avoid(tasks.filter(status=Task.COMPLETE).count(), tasks.count())
        context["render_pie"] = [tasks.filter(status=Task.COMPLETE).count(), tasks.filter(status=Task.PENDING).count(), tasks.filter(status=Task.IN_PROGRESS).count()]
        return context


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member-list')


class MemberUpdateView(UpdateView):
    model = Member
    success_url = reverse_lazy('member-list')


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('member-list')
