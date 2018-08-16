from django.urls import path, include
from . import views

app_name='home'
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('resources/<int:pk>/', views.Resources.as_view(), name = 'resources'),
    path('topics/', views.Topics.as_view(), name = 'topics'),
    path('', views.Home.as_view(), name = 'home'),
]

handler404 = 'Template404.as_view()'
