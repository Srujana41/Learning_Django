from django.shortcuts import render
from todo.models import Task

def home(request):
    # To get data with filter and then arrange data in ascending order add "-" to the field otherwise nothing for descending order
    tasks = Task.objects.filter(is_Completed = False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_Completed = True).order_by('-created_at')
    # print(completed_tasks)
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)