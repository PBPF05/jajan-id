from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUp(UserCreationForm):
    ROLES_CHOICES = [('S', 'Penjual'),
                     ('B', 'Pembeli'),]
    roles = forms.ChoiceField(
        label="Roles",
        required=True,
        choices=ROLES_CHOICES,
        widget=forms.RadioSelect() 
    )

    class Meta:
        model = User
        fields = ['username', 'roles', 'password1']

    def save(self, commit=True):
        user = super(SignUp, self).save(commit=False)
        user.roles = self.cleaned_data["roles"]

        if commit:
            user.save()

        return user