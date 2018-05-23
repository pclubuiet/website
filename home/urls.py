from django.conf.urls import url, handler404
from . import views

app_name='home'
urlpatterns = [
	url(r'^$', views.Home.as_view(), name = 'home'),
	url(r'^resources/', views.Resources.as_view(), name = 'resources'),
	url(r'^events/suggest', views.SuggestEvent.as_view(), name = 'suggest_event'),
	url(r'^events/approve/(?P<pk>[^/]+)', views.ApproveEvent.as_view(), name = 'approve_event'),
	url(r'^events/reject/(?P<pk>[^/]+)', views.RejectEvent.as_view(), name = 'reject_event'),
	url(r'^events/', views.Events.as_view(), name='events'),
]

handler404 = 'Template404.as_view()'
