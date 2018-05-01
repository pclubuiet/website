from django import views
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from datetime import date


class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(views.View):
    def get(self, request, *args, **kwargs):
    	return render(request, "home/resources/resources.html", {'resources': Resource.objects.all()})

class events(views.View):
    def get(self, request, *args, **kwargs):
        events = Events.objects.all()
        for event in events:
            if event.date < date.today():
                event.typeofentry='Past Events'
        return render(request, 'home/events/events.html', {'events': events})
