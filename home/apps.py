from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'

class Resources(TemplateView):
    template_name = 'resources'
