from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(TemplateView):
    template_name = 'resources/resources.html'
