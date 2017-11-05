from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LabStatus(models.Model):
	"""Lab status Model"""

	created_on = models.DateField(auto_now_add=True)
	DayNo = models.IntegerField(default=0)
	status = models.BooleanField(default=True)
	message = models.CharField(max_length=140, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Lab Status"

	def __str__(self):

		return self.status




	    	

class dailyAttendance(models.Model):

	"""Daily Attendence Model"""
	PRESENT = 'p'
	ABSENT = 'a'
	ON_LEAVE = 'l'

	Status_choice = (
	(PRESENT,'Present'),
	(ABSENT,'Absent'),
	(ON_LEAVE,'On leave'),
	)

	user = models.ForeignKey(User)
	status = models.CharField(
		max_length=1,
		choices=Status_choice,
	)

	reason = models.TextField(blank=True)
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Daily Attendence"

	def __str__(self):
		return self.status
	
	


class UserAttendence(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	present_days = models.IntegerField(default=0)
	absent_days = models.IntegerField(default=0)
	on_leave = models.IntegerField(default=0)
	# another field to be added that records the no of leaves in the ongoing month and 
	# becomes 0 at the beginning of new month.
