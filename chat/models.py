from django.db import models

SEX_CHOICES = (
    ('F', 'Female',),
    ('M', 'Male',),
)

SMOKER_CHOICES = (
    ('Y', 'Yes',),
    ('N', 'No',),
)


class Bot(models.Model):
    name = models.CharField("What's your name?", max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField("When were you born?")
    smoker = models.CharField(max_length=1, choices=SMOKER_CHOICES)
