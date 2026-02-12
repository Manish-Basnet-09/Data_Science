
from django.shortcuts import render
from .models import Employee

def index(request):
    datbase_data = Employee.objects.all()

    data_context = {
        "database_data": datbase_data,
        "page_title": "Project Dashboard",
        "company_name": "TechFlow Systems",
        "generated_at": "2023-10-25 14:30",
       
       
        "tasks": [
            {"id": "T-101", "task": "Server Migration", "owner": "Alice", "priority": "High"},
            {"id": "T-102", "task": "Update CSS", "owner": "Bob", "priority": "Low"},
            {"id": "T-103", "task": "Client Meeting", "owner": "Charlie", "priority": "Medium"},
            {"id": "T-104", "task": "Fix Login Bug", "owner": "Alice", "priority": "High"},
        ]
    }
   
    return render(request, 'web_app\index.html', data_context)

# web_app/views.py
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


# View 1: Render the list of data
def employee(request):
    # Fetch ALL employees from the database
    employees = Employee.objects.all().order_by('-created_at')
   
    context = {
        'page_title': 'Staff Directory',
        'staff_list': employees
    }
    return render(request, 'web_app/home.html', context)


# View 2: Handle the Form (GET to show, POST to save)
def add_employee(request):
    if request.method == 'POST':
        # Populate the form with data from the request
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save() # Saves directly to the DB
            return redirect('index') # Redirect back to the list
    else:
        # If GET, show an empty form
        form = EmployeeForm()

    return render(request, 'web_app/add_employee.html', {'form': form})