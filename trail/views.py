from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views import View

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

#function based view
def Home(request):
    
    return render(request,'index.html')

def addEmp(request):
    if request.method == "POST":
        ename = request.POST.get('name')
        esal = request.POST.get('sal')
        ead = request.POST.get('emp')
        data = Employee.objects.create(ename = ename,esal = esal,eaddr = ead)
        data.save()
    
    return render(request,'employee.html')

def delete_obj(request, pk):
    record = Employee.objects.get(id=pk)
    record.delete()
    return redirect('home')

def update_obj(request, pk):
    record = Employee.objects.get(id=pk) # retrieval/ fetching that record 
    context = {'record':record}

    if request.method=="POST":
        name = request.POST.get('name')
        salary = request.POST.get('sal')
        addr = request.POST.get("emp")

        record.ename = name
        record.esal = salary
        record.eaddr = addr
        record.save()
        return redirect('home')
    return render(request,'update.html',context)




