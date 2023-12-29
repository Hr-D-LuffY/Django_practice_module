
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.profile,name='profile'),
]
