from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm

def login(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'loggedIn.html')
    form = EmployeeForm()
    return render(request,'login.html',{'form1':form})

def signup(request):
    return render(request,'signup.html')

def home(request):
    return render(request,'index.html')