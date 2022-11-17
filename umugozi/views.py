from django.shortcuts import render,redirect
from .models import *
from email import message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'index.html')
def register(request):
    selectdata= Person.objects.all()
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        dob=request.POST['dob']
        address=request.POST['address']
        gender=request.POST['gender']
        password=request.POST['password']
        confirm=request.POST['confirm']
        if password == confirm :
            user = User.objects.create_user(username=username,email=email,password=password)
            insertdata= Person(firstname=firstname,lastname=lastname,username=username,email=email,dob=dob,address=address,gender=gender,password=password)
            user.firstname = firstname
            user.lastname = lastname
            user.save()
            print("Account creation success")
        else:
            print("password doesn't match")
        try:
            insertdata.save()
            return render(request, 'register.html',{'data':selectdata})
        except:
            return render(request, 'register.html')
    return render(request, 'register.html',{'data':selectdata})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            return render(request,'index.html')
        else:
            
            print('no match!')
            print("incorrect")
            
    return render(request, 'login.html')
