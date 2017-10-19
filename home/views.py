from django.views.generic import TemplateView, View
from django.shortcuts import render
from .forms import *

class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(TemplateView):
    template_name = 'home/resources/resources.html'

class Register(View):
	registered = False
	
	def get(self, request):
		user_form=UserForm()
		
		return render(request,'home/register/register.html',
			{'user_form':user_form,'registered':self.registered})

	def post(self, request):
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			self.registered=True
		else:
			print(user_form.errors, profile_form.errors)

		return render(request,'home/register/register.html',
			{'user_form':user_form, 'registered':self.registered})