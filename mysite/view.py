from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee
def home(request):
    employee = Employee.objects.all()  # Ensure the Employee model is imported
    print(employee)  # Debugging line to check if employees are fetched
    # Render the home page with a message
    context = {
        'employees': employee,
    }
    print(context) 
    return render(request, "home.html", context)