from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from analytics.utils import get_member_analytics
from .forms import MemberForm
from .models import Member
from tasks.models import Task
from analytics.models import Entry
from sprints.models import Sprint


class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'


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

        entries, sprint = get_member_analytics(self.object)

        context["sprint_list"] = sprint
        context["hours"] = entries

        print(entries)
        print(sprint)




        return context


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member-list')


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member-list')


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('member-list')
