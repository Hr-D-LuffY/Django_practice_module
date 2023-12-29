from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login ,logout

# Create your views here.
def signup(request):
    if request.method=='POST':
        signupform= forms.Registration(request.POST)
        if signupform.is_valid():
            signupform.save()
            messages.success(request,'Account Created Succesfully')
            return redirect('user_login')
    else:
        signupform=forms.Registration()
    return render(request, 'signup.html',{'form': signupform, 'type':'Signup'})

def user_login(request):
    if request.method=='POST':
        loginform= AuthenticationForm(request,request.POST)
        if loginform.is_valid():
            user_name= loginform.cleaned_data['username']
            user_pass= loginform.cleaned_data['password']
            user=authenticate(request, username=user_name , password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request,"Logged in Succesfully")
                return redirect('homepage')
            else:
                messages.warning(request,"Logged Information Incorrect!!")
                return redirect('signup')
    else:
        loginform=AuthenticationForm()
    return render(request, 'signup.html',{'form': loginform, 'type':'Login'})

@login_required
def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    messages.success(request,"Logged out Succesfully")
    return redirect('homepage')
