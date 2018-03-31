from django.forms import ModelForm
from .models import SignUp
from django import forms

class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
            're_password': forms.PasswordInput(),
        }
