from django.conf.urls import url
from . import views
app_name='home'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Home.as_view(), name = 'home'),
    url(r'^resources/', views.Resources.as_view(), name = 'resources')
]
