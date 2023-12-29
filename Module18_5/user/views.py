from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , SetPasswordForm
from django.contrib.auth import authenticate, login ,logout,update_session_auth_hash

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
                return redirect('profile')
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

@login_required
def chng_pass(request):
    if request.method=='POST':
        changpass= PasswordChangeForm(request.user,data=request.POST)
        if changpass.is_valid():
            changpass.save()
            messages.success(request,'Password Updated Succesfully')
            update_session_auth_hash(request,changpass.user)
            return redirect('profile')
    else:
        changpass=PasswordChangeForm(user= request.user)
    return render(request, 'changePass.html',{'form': changpass})

@login_required
def chng_pass_without(request):
    if request.method=='POST':
        changpass= SetPasswordForm(request.user,data=request.POST)
        if changpass.is_valid():
            changpass.save()
            messages.success(request,'Password Updated Succesfully')
            update_session_auth_hash(request,changpass.user)
            return redirect('profile')
    else:
        changpass=SetPasswordForm(user= request.user)
    return render(request, 'changePass.html',{'form': changpass})
