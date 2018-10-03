from django.urls import path, include
from . import views

app_name='home'
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('resources/<int:pk>/', views.Resources.as_view(), name = 'resources'),
    path('blog/<int:pk>/', views.BlogPostView.as_view(), name = 'blog_post'),
    path('blog/', views.BlogPostList.as_view(), name = 'blog'),
    path('topics/', views.Topics.as_view(), name = 'topics'),
    path('', views.Home.as_view(), name = 'home'),
    path('leaderboard/', views.Leaderboard.as_view(), name = 'leaderboard'),
    path('github_email_check/', views.GithubEmailCheck, name = 'github_email_check'),
    path('github_check/', views.GithubCheck, name = 'github_check'),
    path('registeruser/', views.RegisterUser.as_view(), name = 'registeruser'),
]

handler404 = 'Template404.as_view()'
