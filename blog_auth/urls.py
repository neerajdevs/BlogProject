
from django.contrib import admin
from django.urls import path,include
from .views import login , registration

urlpatterns = [
    path('login' , login , name='login' ),
    path('register' , registration , name='register' ),
] 
