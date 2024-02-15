from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=500)
    img_url = models.CharField(max_length=500)


