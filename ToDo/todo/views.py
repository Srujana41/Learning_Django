from django.shortcuts import redirect, get_object_or_404, render
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

def markAsDone(request, pk):
    # mark task as done
    task = get_object_or_404(Task, pk=pk)
    task.is_Completed = True
    task.save()
    return redirect('home')

def markAsUndone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_Completed = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    task_get = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task_get.task = new_task
        task_get.save()
        return redirect('home')
    else:
        context ={
            'task_get':task_get
        }
        return render(request, "edit-task.html", context)
    
def deleteTask(request, pk):
    task= get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
