from django.urls import path,include
from . import view

urlpatterns = [
    path('',view.index),
]