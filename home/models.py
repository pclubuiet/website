from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=128, blank=False, null=True)
    url = models.URLField(max_length=128, db_index=True, blank=False, null=True)

    def __str__(self):
    	return self.title