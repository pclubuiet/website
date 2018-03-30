from django.db import models

class SignUp(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name
