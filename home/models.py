from django.db import models


class Resource(models.Model):
	""" A resource that shows students the name of the language, example, and an image. """
	image = models.ImageField() 	# Might need to install Pillow for ImageField to work.
	language = models.CharField(max_length=30)
	example = models.TextField()

	def __str__(self):
		return "%s" % (self.language)

class Resources(models.Model):
	resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
	headline = models.CharField(max_length=100)
	pub_date = models.DateField()

	def __str__(self):
		return self.headline

	class Meta:
		ordering = ('headline',)


