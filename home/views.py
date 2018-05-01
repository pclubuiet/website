from django import views
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
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

class suggest_events(CreateView):
    model = Events
    fields = ['title', 'url', 'image', 'brief', 'date']
    template_name = 'home/events/suggest_events.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.suggested_by = self.request.user.pk
        return super(suggest_events, self).form_valid(form)
