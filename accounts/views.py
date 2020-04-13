from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import register
from django.contrib import messages

def registerPage(request):
    # form = CreateUserForm()

    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        # assert isinstance(User.objects.create_user,)
        x = register(username=username, email=email, password1=password1, password2=password2)
        x.save()
        print("User Successfully Created")
        return redirect("/")
    else:
        return render(request,'accounts/register.html')

def home(request):
    return render(request,'accounts/dashboard.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            #auth.login(request,user)
            return redirect('chat/index/')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect("/")
    else:
        return render(request,'accounts/login.html')

def customers(request):
    return render(request,'accounts/customers.html')

def products(request):
    return render(request,'accounts/products.html')
