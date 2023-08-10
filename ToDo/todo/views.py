from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
#getting data from post request
def addTask(request):
    #to print post request contents in terminal
    #print(request.POST['task']) 
    task = request.POST['task']
    #to create task in database by sending task entered by user
    Task.objects.create(task=task)
    #redirect user back to home page after clicking on add button
    return redirect('home')
