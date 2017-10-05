from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
app_name='home'
urlpatterns = [
    url(r'$', views.Home.as_view(), name='home'),
    url(r'^home/$', RedirectView.as_view(url='/home/')),
    url(r'^resources/$', views.Resources.as_view(), name = 'resources')
]
