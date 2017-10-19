from django.views.generic import TemplateView, View
from django.shortcuts import render
from .forms import *

class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(View):
	validated = False
	
	def get(self, request):
		profile_form = ProfileForm
		
		return render(request,'home/resources/resources.html',
			{'profile_form':profile_form,'validated':self.validated})

	def post(self, request):
		profile_form = ProfileForm(data=request.POST)
		if profile_form.is_valid():
			profile=profile_form.save(commit=False)
			profile.user=request.user
			profile.save()
			self.validated=True
		
		else:
			print(profile_form.errors)

		return render(request,'home/resources/resources.html',
			{'profile_form':profile_form, 'validated':self.validated})

class Register(View):
	registered = False
	
	def get(self, request):
		user_form=UserForm()
		profile_form = ProfileForm
		
		return render(request,'home/register/register.html',
			{'user_form':user_form,'profile_form':profile_form,'registered':self.registered})

	def post(self, request):
		user_form = UserForm(data=request.POST)
		profile_form = ProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()
			self.registered=True
		
		else:
			print(user_form.errors, profile_form.errors)

		return render(request,'home/register/register.html',
			{'user_form':user_form,'profile_form':profile_form, 'registered':self.registered})