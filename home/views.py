from django import views
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import *


class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Topics(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/resources/topics.html", {'topics': Resource.objects.all()})

class Resources(views.View):
    def get(self, request, pk, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=pk)
        return render(request, "home/resources/resources.html", {'resources': topic.resource_set.all(), 'topic' : topic})
