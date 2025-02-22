from django.contrib.messages.views import SuccessMessageMixin
from django.forms import modelformset_factory, TextInput
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from analytics.utils import get_member_sprint, get_sprint_data, get_daily_average, get_sum
from tasks.models import Task
from .forms import MemberForm
from .models import Member


class MemberListView(ListView):
    model = Member


class MemberDetailView(DetailView):
    model = Member

    def get_context_data(self, **kwargs):
        def division_zero_avoid(arg1, arg2):
            if arg1 == 0 or arg2 == 0:
                return 0
            return (arg1 / arg2) * 100

        context = super(MemberDetailView, self).get_context_data(**kwargs)
        tasks = Task.objects.all().filter(assignee=self.object)
        context["tasks"] = tasks.count()

        context["tasks_done"] = division_zero_avoid(
            tasks.filter(status=Task.COMPLETE).count(), tasks.count())

        context["render_pie"] = [tasks.filter(status=Task.COMPLETE).count(),
                                 tasks.filter(status=Task.PENDING).count(),
                                 tasks.filter(status=Task.IN_PROGRESS).count(),
                                 tasks.filter(status=Task.OVERDUE).count()]

        context["OVERDUE"] = Task.OVERDUE

        sprints = get_member_sprint(self.object)
        context["sprint_list"] = sprints.all()
        print("views1", sprints.all())

        # dictionary of lists
        context["data"] = {"dates": [], "hours": [], "sum": [], "avg": [], }

        for q in sprints.all():
            # print('views', q)
            dates, hours = get_sprint_data(q, self.object)
            context["data"]["dates"].append(dates)  # [sprint1_dates, sprint2_dates]
            context["data"]["hours"].append(hours)

            total = get_sum(q, self.object)
            average = get_daily_average(q, self.object)

            # print(total)
            # print('views', average)
            context["data"]["sum"].append(total)
            context["data"]["avg"].append(average)

        # print(sprints)
        # print(context['data']['dates'])
        # print(context['data']['hours'])
        # print(context['data']['avg'])

        return context


class MemberCreateView(SuccessMessageMixin, CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member-list')
    success_message = '%(first_name)s %(last_name)s was successfully added to the team'


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member-list')


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('member-list')


def member_formset(request):
    MemberFormSet = modelformset_factory(
        Member,
        fields=('first_name', 'last_name', 'email'),
        labels={
            'first_name': '',
            'last_name': '',
            'email': '',
        },
        widgets={
            'first_name': TextInput(attrs={'style': 'width:260px'}),
            'last_name': TextInput(attrs={'style': 'width:260px'}),
            'email': TextInput(attrs={'style': 'width:450px'})
        },
        extra=0,
    )

    if request.method == 'POST':
        form = MemberFormSet(request.POST)
        instances = form.save(commit=False)

        for instance in instances:
            instance.save()

    form = MemberFormSet()
    return render(request, 'members/member_formset.html', {'form': form})
