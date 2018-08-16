from django.db import models
from tinymce.models import HTMLField

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
