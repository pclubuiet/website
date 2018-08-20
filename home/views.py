from django import views
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import *


class Template404(TemplateView):
    template_name = "404.html"

class Home(TemplateView):
    template_name = 'home/home.html'

class Topics(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/resources/topics.html", {'topics': Topic.objects.all()})

class Resources(views.View):
    def get(self, request, pk, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=pk)
        return render(request, "home/resources/resources.html", {'resources': topic.resource_set.all(), 'topic' : topic})

class BlogPostList(views.View):
    def get(self, request, *args, **kwargs):
        posts = BlogPost.objects.all()
        return render(request, "home/blog/index.html", {'posts': posts})

class BlogPostView(views.View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(BlogPost, pk=pk)
        return render(request, "home/blog/blog_post.html", {'post': post})
