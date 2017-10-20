from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField(max_length=30)
    year = models.IntegerField()
    branch = models.CharField(max_length=30)
    interests = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: \n '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return self.user.username
