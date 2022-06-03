from django.db import models

# Create your models here.
class Userinfo(models.Model):
    name = models.CharField(max_length=70)
    link = models.CharField(max_length=1000)

