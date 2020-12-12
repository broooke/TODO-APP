from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
	"""docstring for TaskForm"""
	class Meta:
		model = Task
		fields = '__all__'

			
		