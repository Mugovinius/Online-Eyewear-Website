from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm
# Create your views here.
def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out"))
    return redirect('index')

def register_user(request):
    if request.method =="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #after registered, log them in
            customer = authenticate(username=username,password=password)
            login(request,customer)
            messages.success(request,("Registration succesful"))
            return redirect("index")
    else:
        form = RegisterUserForm()
    return render(request,"authenticate/register.html",{'form':form})

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        customer = authenticate(request,username=username,password=password)
        if customer is not None:
            login(request,customer)
            return redirect('index')
        else:
            messages.success(request,("There was an error,Try again!"))
            return redirect('login')
    else:
        return render(request,"authenticate/login.html")

