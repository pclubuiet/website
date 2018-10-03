from django import forms
from .models import Users

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('pr_count',)