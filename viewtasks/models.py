from django.db import models

# Create your models here.

class Task(models.Model):
	"""docstring for Task"""
	title = models.CharField(max_length=300)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class TaskCompleted(models.Model):
	"""docstring for TaskCompleted"""
	title_completed = models.CharField(max_length=300)

	def __str__(self):
		return self.title_completed
		

	

