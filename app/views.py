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


@login_required(login_url='/login/')
def home(request):
	user = get_object_or_404(User, username=request.user.username)
	return render(request, "registration/base.html", {'user': user})


