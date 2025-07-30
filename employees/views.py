from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee
from django.shortcuts import get_object_or_404

# Create your views here.
def employee_details(request, pk):
    #---------->  one to do this 
    # try:
    #     employee = Employee.objects.get(pk=pk)
    #     return HttpResponse(f"Employee: {employee.first_name} {employee.last_name} - {employee.designation}")
    # except Employee.DoesNotExist:
    #     return HttpResponse("Employee not found", status=404)
    # -------------> another way to do this
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee
    }
    return render(request, "employee.html", context)
    
    # Agar employee mil gaya toh response return karo
