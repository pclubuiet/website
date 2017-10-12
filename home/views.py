from django.views.generic import TemplateView

class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Resources(TemplateView):
    template_name = 'home/resources/resources.html'
