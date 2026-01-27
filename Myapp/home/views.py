from django.shortcuts import render

# Create your views here.
# views.py

def index(request):
    context={
        'name':"Manish",
        'age':21,
        'address':"Khotang",
        'courses':"Data science in python"
        }
    return render(request, 'home/home.html',context)

def service(request):
    context={
        'service1':"Web Development",
        'service2':"App Development",
        'service3':"Data Analysis",
        'service4':"Machine Learning"
        }
    return render(request, 'home/service.html',context)

