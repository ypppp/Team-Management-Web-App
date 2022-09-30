from django import forms

from sprints.models import Sprint


class SprintForm(forms.ModelForm):

    class Meta:
        model = Sprint
        fields = [
            'title',
            'sprint_goal',
            'start_date',
            'end_date',
        ]

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        if start_date > end_date:
            raise forms.ValidationError
        return end_date