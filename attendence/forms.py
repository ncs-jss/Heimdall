from django import forms
from . models import dailyAttendance

class AttendanceForm(forms.Form):

	
	class Meta:
		model = dailyAttendance
		fields = ['status']
		