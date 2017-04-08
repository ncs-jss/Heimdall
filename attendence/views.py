from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from app.models import Member
from models import LabStatus, DailyAttendance, UserAttendence
from forms import AttendanceForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

class AttendanceView(View):
	form = AttendanceForm()
	
	@method_decorator(login_required)	
	def get(self, request):
		user = User.objects.all()
		print self.form.errors
		return render(request,"daily_att.html", {'user': user, 'form':self.form})
	
	@method_decorator(csrf_protect)
	def post(self, request):
		pass	