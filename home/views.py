from django import views
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import *


class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(views.View):
    def get(self, request, *args, **kwargs):
    	return render(request, "home/resources/resources.html", {'resources': Resource.objects.all()})

class ResourcePage(views.View):
    def get(self, request, pk, *args, **kwargs):
    	resource = get_object_or_404(Resource, pk=pk)
    	print(resource)
    	return render(request, "home/resources/resource.html", {'resources': resource.resourceurl_set.all(),
    															'resource' : resource})
