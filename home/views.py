from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(TemplateView):
    template_name = 'home/resources/resources.html'
