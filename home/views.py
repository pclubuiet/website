from django import views
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(views.View):
    def get(self, request, *args, **kwargs):
    	return render(request, "home/resources/resources.html", {'resources': Resource.objects.all()})