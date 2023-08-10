from django.shortcuts import render
from todo.models import Task

def home(request):
    # To get data with filter and then arrange data in ascending order add "-" to the field otherwise nothing for descending order
    tasks = Task.objects.filter(is_Completed = False).order_by('-updated_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)