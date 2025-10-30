from django.urls import path
from .views import *

urlpatterns = [
path('' , dashboard , name = 'dashboard'),
path('category' , category_dashboard , name = 'category_dashboard'),
] 
