from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import forms

# Create your views here.
def index(request):
	return render(request, "index.html")

def login(request):
	if request.method=='POST':
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('main', args=[user.username]))
	form = forms.LoginForm()
	return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def home(request, username):
	return HttpResponse("Hello, %s." % username)

@login_required(login_url='/login/')
def logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
