from django.db import models


class SignUp(models.Model):
    year_choices = (
    (1,'I'),
    (2, 'II'),
    (3,'III'),
    (4,'IV'),
    )
    branch_choices = (
    ('CSE', 'CSE'),
    ('IT', 'IT'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('Mech', 'Mech'),
    ('BioTech', 'BioTech'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)
    year = models.IntegerField(choices=year_choices, default=1)
    branch = models.CharField(max_length=20, choices = branch_choices, default='CSE')
    Interests = models.CharField(max_length=20)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
