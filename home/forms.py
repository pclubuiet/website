from django.contrib.auth.models import User
from django import forms
from django.core import validators

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model=User
		fields=('username','password','email')
	def clean_username(self):
		cleaned_data=super().clean()
		username=self.cleaned_data['username']
		if User.objects.filter(username__iexact=username):
		 	raise forms.ValidationError('Username taken')
		else:
			pass
		return username