from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):	

	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	year = models.IntegerField()
	club = models.CharField(max_length=32, default=" ")
	admNo = models.CharField(max_length=10)
	contactNo = models.CharField(max_length=10)
	github = models.CharField(max_length=100)
	codechef = models.CharField(max_length=100, blank=True, null=True)
	Behance = models.CharField(max_length=100, blank=True, null=True)
	facebook = models.CharField(max_length=100)
	warnings = models.IntegerField(default=0)