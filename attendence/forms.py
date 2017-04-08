from django import forms
from models import DailyAttendance

class AttendanceForm(forms.Form):
	class Meta:
		model = DailyAttendance
		fields = ['user', 'status']
		