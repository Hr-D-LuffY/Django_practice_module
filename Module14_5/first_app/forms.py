from django import forms
from . import models
import datetime

BIRTH_YEAR_CHOICES = [x for x in range(1980,2000)]
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=30,initial='Your Name')
    comment= forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':50}))
    email =forms.EmailField(required=False,label='Enter your Email')
    age=forms.IntegerField(help_text='Enter ur Age')
    agree= forms.BooleanField()
    password=forms.CharField(widget=forms.PasswordInput, required=False)
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colorinRadio = forms.ChoiceField(widget=forms.RadioSelect ,choices=FAVORITE_COLORS_CHOICES)
    favorite_multicolorincheck = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple ,choices=FAVORITE_COLORS_CHOICES)

class Exam2(forms.ModelForm):
    class Meta:
        model= models.example
        fields ='__all__'