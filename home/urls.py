from django.conf.urls import url, handler404
from . import views

app_name='home'
urlpatterns = [
url(r'^$', views.Home.as_view(), name = 'home'),
url(r'^resources/', views.Resources.as_view(), name = 'resources'),
url(r'events/suggest', views.suggest_events.as_view(), name = 'suggest_events'),
url(r'^events/', views.events.as_view(), name='events'),
]

handler404 = 'Template404.as_view()'
