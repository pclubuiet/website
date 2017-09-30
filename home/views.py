from django.views.generic import TemplateView
from django.shortcuts import render


class Home(TemplateView):
    template_name = 'home.html'

class Resources(TemplateView):
    template_name = 'resources.html'
