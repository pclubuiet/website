from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=128, blank=False, null=True)
    
    def __str__(self):
    	return self.title

class ResourceURL(models.Model):
	title = models.CharField(max_length=128, blank=False, null=True)
	url = models.URLField(max_length=128, db_index=True, blank=False, null=True)
	resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
	category = models.CharField(max_length=128, blank=False, null=True, choices=(("video", "Videos"),
																				 ("blog", "Blogs / Articles"),
																				 ("ebook", "E-Books"),
																				 ("other", "Others"),))
	def __str__(self):
		return self.title + " (" + str(self.resource) + ")"