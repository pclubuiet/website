from django import views
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import *
from .forms import *
import requests
import http
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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

class Leaderboard(views.View):
    def get(self, request, *args, **kwargs):
        users = Users.objects.all()
        for user in users:
            connected = False
            while not connected:
                try:
                    user_name = user.github_handle
                    response = requests.get('https://api.github.com/search/issues?sort=created&q=author:{}&type:pr&per_page=100'.format(user_name), verify = False).json()
                    pr_count = 0
                    print(response)
                    for obj in response['items']:
                        if('pull_request' in obj):
                            if('2018-09-30T00:00:00Z'<obj['created_at']<'2018-10-31T23:59:59Z'):
                                pr_count += 1
                    user.pr_count = pr_count
                    user.save()
                    connected = True
                except:
                    pass
        return render(request, 'home/leaderboard.html', {'users': users})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "home/registeruser.html"
    success_url = reverse_lazy('home:home')

@csrf_exempt
def GithubEmailCheck(request):
    github_handle = request.POST.get('github_handle')
    email = request.POST.get('email')
    print("Received ", github_handle)
    users = Users.objects.all()
    for user in users:
        if user.github_handle == github_handle:
            return JsonResponse({'message' : 'Duplicate Github Handle'})
        if user.email == email:
            return JsonResponse({'message' : 'Duplicate Email'})
    return JsonResponse({'message' : 'New'})

@csrf_exempt
def GithubCheck(request):
    github_handle = request.POST.get('github_handle')
    response = requests.get("https://api.github.com/users/{}".format(github_handle), verify = False).json()
    print("https://api.github.com/users/{}".format(github_handle))
    if ('login' in response):
        print("Found")
        return JsonResponse({'message' : 'Found'})
    else:
        return JsonResponse({'message' : 'Not Found'})