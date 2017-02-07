from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Attendance(models.Model):
	user = models.ForeignKey(User)
	total_days = models.IntegerField(default=0)
	present_days = models.IntegerField(default=0)
	absent_days = models.IntegerField(default=0)
	reason = models.TextAreaField(null=True)
	informed = models.CharField(max_length=40)