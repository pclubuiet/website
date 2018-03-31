from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SignUpView.as_view(), name='signup'),
]
