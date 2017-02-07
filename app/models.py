from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length=32)
	year = models.IntegerField()
	roll = models.CharField(max_length=10)
	contactNo = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	github = models.CharField(max_length=100)
	facebook = models.CharField(max_length=100)
