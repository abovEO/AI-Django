from django.db import models


# Create your models here.
class Userinfo(models.Model):
    name = models.CharField(max_length=70)
    link = models.CharField(max_length=1000)

class datacaptb(models.Model):
    fname = models.CharField(max_length=70)
    imgcount= models.IntegerField()
    clink = models.CharField(max_length=2000)
