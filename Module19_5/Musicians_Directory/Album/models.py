from django.db import models
from musician.models import Musician

from django import forms
from django.forms.widgets import NumberInput
rating=[
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4),
    ('5',5),
]

# Create your models here.
class Album(models.Model):
    Album_name= models.CharField(max_length=50)
    release_date= models.DateField()
    rating= models.CharField(max_length=1,choices=rating)
    musician=models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.Album_name
    
