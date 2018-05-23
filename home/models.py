from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=128, blank=False, null=True)
    url = models.URLField(max_length=128, db_index=True, blank=False, null=True)

    def __str__(self):
    	return self.title

class Event(models.Model):
    class Meta:
        permissions = (
            ('approve_suggestion', 'Approve a suggested event'),
        )
    title = models.CharField(max_length=128, blank=False, null=True)
    image=models.FileField(upload_to='events_images/')
    brief = models.CharField(max_length=500, blank=False, null=True)
    url = models.URLField(max_length=128, db_index=True, blank=False, null=True)
    date=models.DateField()
    typeofentry=models.CharField(max_length=20, choices = (("past", "Past Event"),
                                                           ("upcoming", "Upcoming Event"),
                                                           ("suggested", "Suggested Event")) , default='suggested')
    suggested_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title