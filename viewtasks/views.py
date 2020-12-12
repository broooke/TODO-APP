from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task, TaskCompleted
from .forms import *

# Create your views here.

def home(request):
	tasks = Task.objects.all()
	tasks_completed = TaskCompleted.objects.all()
	form = TaskForm()
	if request.method=='POST':
	 	form = TaskForm(request.POST)
	 	if form.is_valid():
	 		form.save()
	 	return redirect('/')
	# try:
	#  	for i in tasks:
	#  		if i.complete==True:
	#  			a.append(i.title)
	# except Exception as e:
	#  	return redirect('/')

	dictionary = {'tasks':tasks, 'form':form, 'tasks_completed': tasks_completed}
	return render(request,'home.html', dictionary)

def update(request, task_id):
	task = Task.objects.get(id=task_id)
	form = TaskForm(instance=task)
	if request.method=='POST':
	 	form = TaskForm(request.POST, instance=task)
	 	if form.is_valid():
	 		form.save()
	 		return redirect('/')

	dictionary = {'task':task, 'form':form}
	return render(request, 'update.html', dictionary)

def delete(request,task_id):
	task = Task.objects.get(id=task_id)
	task.delete()
	return redirect('/')

def complete(request,task_id):
	task = Task.objects.get(id=task_id)
	task_completed = TaskCompleted(title_completed=task.title)
	task.delete()
	task_completed.save()
	return redirect('/')

def deletecompleted(request,task_id):
	task = TaskCompleted.objects.get(id=task_id)
	task.delete()
	return redirect('/')





# def add(request):
# 	task = Task(title=request.POST['add'])
# 	task.save()
# 	return HttpResponseRedirect('../')



