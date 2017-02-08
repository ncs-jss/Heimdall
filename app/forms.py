from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):

	username = forms.CharField(
								label='username', 
								max_length=30, 
								widget = forms.TextInput(attrs={'placeholder': 'Username', 'name': 'fname'})
							)
	password = forms.CharField(
		label='password', 
		widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'name': 'pword'})
		)
