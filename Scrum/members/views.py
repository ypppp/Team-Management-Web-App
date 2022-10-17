from django.core.checks import messages
from django.forms import modelformset_factory, Textarea, CharField, TextInput
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView, FormView)
from django.views.generic.detail import SingleObjectMixin

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
        context["render_pie"] = [tasks.filter(status=Task.COMPLETE).count(), tasks.filter(status=Task.PENDING).count(),
                                 tasks.filter(status=Task.IN_PROGRESS).count()]
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


def memberFormset(request):
    MemberFormSet = modelformset_factory(
        Member, fields=('first_name', 'last_name', 'email'),
        widgets={'first_name': TextInput(attrs={'style': 'width:250px'}),
                 'last_name': TextInput(attrs={'style': 'width:250px'}),
                 'email': TextInput(attrs={'style': 'width:350px'})}
    )

    if request.method == 'POST':
        form = MemberFormSet(request.POST)
        instances = form.save(commit=False)

        for instance in instances:
            instance.save()

    form = MemberFormSet()
    return render(request, 'members/member_formset.html', {'form': form})
