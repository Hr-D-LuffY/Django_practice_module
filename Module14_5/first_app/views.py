from django.shortcuts import render
from . import forms
# Create your views here.
def home(request):
    form= forms.ExampleForm
    form2= forms.Exam2
    return render(request,'home.html',{'forms':form,'form2':form2})