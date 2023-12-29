from django.shortcuts import render,redirect
from . import forms
from .models import Album
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_album(request):
    if request.method == 'POST':
        album_form= forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form= forms.AlbumForm()
    return render(request,'add_album.html',{'form':album_form})
@login_required
def edit_album(request,id):
    post=Album.objects.get(pk=id)
    album_form= forms.AlbumForm(instance=post)
    if request.method == 'POST':
        album_form= forms.AlbumForm(request.POST,instance=post)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')

    return render(request,'add_album.html',{'form':album_form})

