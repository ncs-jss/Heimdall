from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LabStatus(models.Model):
	created_on = models.DateField(auto_now_add=True)
	DayNo = models.IntegerField(default=0)
	status = models.BooleanField(default=True)
	message = models.CharField(max_length=140, blank=True, null=True)

	class Meta:
		verbose_name_plural="Lab Status"

class DailyAttendance(models.Model):
	
	STATUS_CHOICES = (
    (1, " "),
    (2, "Present"),
    (3, "Absent"),
    (4, "On Leave")
	)
	user = models.ForeignKey(User)
	date = models.DateField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS_CHOICES, default=1)

class UserAttendence(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	present_days = models.IntegerField(default=0)
	absent_days = models.IntegerField(default=0)
	on_leave = models.IntegerField(default=0)
	# another field to be added that records the no of leaves in the ongoing month and 
	# becomes 0 at the beginning of new month.
