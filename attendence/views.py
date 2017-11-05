from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView

from models import LabStatus, dailyAttendance, UserAttendence
from app.models import MemberProfile


from forms import AttendanceForm

# Create your views here.

class AttendanceView(View):
	form = AttendanceForm()
	
	#@method_decorator(login_required)	
	def get(self, request):
		users = User.objects.all()
		print self.form.errors
		return render(request, "attendence/attendance.html", {'users': users})
	
	@method_decorator(csrf_protect)
	def post(self, request, uid):
		
		form_data = self.form(self.request.POST)
		if form_data.is_valid():

			user = User.objects.get(id=uid).id
			status = form_data.cleaned_data['status']

			form_data.save()
			return HttpResponseRedirect('/attendance/')



class AttendanceListView(ListView):
	
	template_name = ""
	model = UserAttendence

 	def get_context_data(self):

 		return UserAttendence.objects.all()



#login required decorater
class AttendenceDetailView(DetailView):

	template_name = "xyz.html"
	model = dailyAttendance

	@method_decorator(login_required)
	def get_context_data(self):
		
		return dailydAttendence.objects.all()



class TakingAttendenceView(object):
	"""Taking Attendence View"""

	@method_decorator(login_required)
	def takingAttendence(self, request):

		user = User.objects.get(username = request.user.username)
		

		
