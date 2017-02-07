from django.shortcuts import (render, 
								get_object_or_404, redirect)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import forms

# Create your views here.
def index(request):
	return render(request, "index.html")

def login_page(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home/')
	form = forms.LoginForm()
	return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def home(request):
	user = get_object_or_404(User, username=request.user.username)
	return HttpResponse("Hello, %s." % user.username)

@login_required(login_url='/login/')
def logout_page(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
