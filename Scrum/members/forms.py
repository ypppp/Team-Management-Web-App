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

    nickname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'What do they call you?'}),
        required=False
    )

    class Meta:
        model = Member
        fields = [
            'first_name',
            'last_name',
            'email',
            'nickname',
        ]

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if ' ' in nickname:
            raise forms.ValidationError('Must not contain spaces')
        return nickname
