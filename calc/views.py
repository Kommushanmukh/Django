from django.shortcuts import render
from . models import *

def home(request):
    return render(request,'home.html',{'name':'Shanmukh'})

def bmi(request):
    w=float(request.POST['weight'])
    h=float(request.POST['height'])
    
    mybmi=w/(h**2)

    return render(request,'bmi.html',{'bmi':mybmi})

def dashboard(request):
    customers=Customer.objects.all()
    return render(request,'dashboard.html',{'customers':customers})

def products(request):
    products=Products.objects.all()
    return render(request,'products.html',{'products':products})


