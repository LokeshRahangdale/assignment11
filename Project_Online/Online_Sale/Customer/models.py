from django.db import models

# Create your models here.
class RegisterData(models.Model):
	name = models.CharField(max_length=50)
	contact = models.CharField(max_length=10)
	address = models.CharField(max_length=64)
	email = models.EmailField()
	password = models.CharField(max_length=12)