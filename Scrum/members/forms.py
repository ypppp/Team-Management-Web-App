from django import forms

from members.models import Member


class MemberForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Member\'s first name'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Member\'s last name'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Member\'s email address'})
    )

    class Meta:
        model = Member
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
