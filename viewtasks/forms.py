from django.forms import ModelForm
from .models import Task
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(ModelForm):
	"""docstring for TaskForm"""
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
	

			
		