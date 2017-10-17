from django.conf.urls import url, handler404
from . import views

app_name='home'
urlpatterns = [
url(r'^$', views.HomeView, name = 'home'),
url(r'^resources/', views.ResourceView, name = 'resources')
]

handler404 = 'Template404.as_view()'

