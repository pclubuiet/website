from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Topic(models.Model):
  title = models.CharField(max_length=128, blank=False, null=True)

  def __str__(self):
    return self.title

class Resource(models.Model):
  title = models.CharField(max_length=128, blank=False, null=True)
  url = models.URLField(max_length=128, db_index=True, blank=True, null=True)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  description = HTMLField()
  category = models.CharField(max_length=128, blank=False, null=True, choices=(("video", "Videos"), ("blog", "Blogs / Articles"), ("ebook", "E-Books"), ("other", "Others"),))

  def __str__(self):
    return self.title + " (" + str(self.topic) + ")"

class BlogPost(models.Model):
  title = models.CharField(max_length=128, blank=False, null=True)
  description = models.CharField(max_length=128, blank=True, null=True)
  body = HTMLField()
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
class Users(models.Model):
  name = models.CharField(max_length = 100)
  year = models.CharField(max_length = 10, choices = (('','Choose Year'),('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')))
  branch = models.CharField(max_length = 100, choices = (('','Choose Branch'), ('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Mech', 'Mech'), ('Bio Tech', 'Bio Tech')))
  github_handle = models.CharField(max_length = 100, unique = True)
  email = models.EmailField(unique = True)
  pr_count = models.PositiveIntegerField(default = 0)

  def __str__(self):
    return self.name + " | " + self.github_handle