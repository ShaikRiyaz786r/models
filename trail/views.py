from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    data = {'name':'rohan'}
    return render(request,'login.html',data)

def signup(request):
    return render(request,'signup.html')

def home(request):
    return render(request,'index.html')