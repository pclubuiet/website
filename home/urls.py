from django.conf.urls import url
from . import views
app_name='home'
urlpatterns = [
url(r'^$', views.HomeView, name = 'home'),
url(r'^resources/', views.ResourceView, name = 'resources')
]
