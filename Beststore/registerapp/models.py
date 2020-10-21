from django.contrib.auth.models import AbstractUser
from django.db import models 

class User(AbstractUser):
	address = models.CharField(max_length=55)

class Product(models.Model):
	name = models.CharField(max_length = 50)
	price = models.CharField(max_length=10)
	image = models.FileField(upload_to=None, max_length=254)
	description = models.TextField()
	manufacturer = models.CharField(max_length=300,blank=True)