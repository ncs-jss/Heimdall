from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect

from models import LabStatus, DailyAttendance, UserAttendence
from app.models import Member

from forms import AttendanceForm

# Create your views here.

class AttendanceView(View):
	# form = AttendanceForm()
	
	@method_decorator(login_required)	
	def get(self, request):
		users = User.objects.all()
		print self.form.errors
		return render(request, "daily_att.html", {'users': users})
	
	@method_decorator(csrf_protect)
	def post(self, request, uid):
		
		form_data = self.form(self.request.POST)
		if form_data.is_valid():

			user = User.objects.get(id=uid).id
			status = form_data.cleaned_data['status']

			form_data.save()
			return HttpResponseRedirect('/attendance/')


