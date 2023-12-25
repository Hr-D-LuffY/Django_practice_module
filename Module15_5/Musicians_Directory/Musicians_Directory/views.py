from django.shortcuts import render
from Album.models import Album
from musician.models import Musician

# Create your views here.
def home(request):
    musician=Musician.objects.all()
    album=Album.objects.all()
    print(musician)
    print(album)
    return render(request,'home.html',{'musician':musician, 'album':album})