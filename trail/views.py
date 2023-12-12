from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def loginPage(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pd = request.POST.get('password')
        user = authenticate(request,username=un,password=pd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('<center><h1>invalid credientials</h1></center>')
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pd = request.POST.get('password')
        myuser = User.objects.create_user(username=un,password=pd)
        myuser.save()
        return redirect('login')
    return render(request,'signup.html')

def home(request):
    return render(request,'index.html')