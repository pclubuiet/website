from django.conf.urls import url, handler404
from . import views

app_name='home'
urlpatterns = [
url(r'^$', views.Home.as_view(), name = 'home'),
url(r'^resources/', views.Resources.as_view(), name = 'resources'),
url(r'^register/', views.Register.as_view(), name = 'register')
]

handler404 = 'Template404.as_view()'

