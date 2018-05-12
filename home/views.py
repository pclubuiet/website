from django import views
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import *
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse


class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(views.View):
    def get(self, request, *args, **kwargs):
    	return render(request, "home/resources/resources.html", {'resources': Resource.objects.all()})

class Events(views.View):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all()

        for event in events:
            if event.date < date.today():
                event.typeofentry='Past Events'

        past_events = events.filter(typeofentry="past")
        upcoming_events = events.filter(typeofentry="upcoming")
        suggested_events = []
        approved_events = []
        if request.user.has_perm('home.approve_suggestion'):
            suggested_events = events.filter(typeofentry="suggested")
        else:
            if request.user.is_authenticated:
                suggested_events = events.filter(typeofentry="suggested", suggested_by=request.user.pk)
        approved_events = events.filter(typeofentry__in=['upcoming','past'], suggested_by=request.user.pk)
        return render(request, 'home/events/events.html', {'past': past_events, 'upcoming': upcoming_events,
                                                           'suggested': suggested_events, 'approved': approved_events})

class SuggestEvent(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Event
    fields = ['title', 'url', 'image', 'brief', 'date']
    template_name = 'home/events/suggest_events.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.suggested_by = self.request.user.pk
        return super(SuggestEvent, self).form_valid(form)

class ApproveEvent(LoginRequiredMixin, views.View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.has_perm('home.approve_suggestion'):
            event = Event.objects.get(pk=pk)
            event.typeofentry = "upcoming"
            event.save()
            return HttpResponseRedirect(reverse('home:events'))
        else:
            return Http404

class RejectEvent(LoginRequiredMixin, views.View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.has_perm('home.approve_suggestion'):
            event = Event.objects.get(pk=pk)
            event.delete()
            return HttpResponseRedirect(reverse('home:events'))
        else:
            return Http404
