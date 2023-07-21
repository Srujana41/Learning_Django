from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(request):
    # return HttpResponse("Hello")
    # return HttpResponse("<h3>Hello using HTML tag</h3>")
    # return render(request, 'home.html')
    employees = Employee.objects.all()
    # print(employees)
    context = {
        'employees': employees,
    }
    return render( request, 'home.html', context)