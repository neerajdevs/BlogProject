from django.urls import path
from .views import *

urlpatterns = [
path('' , dashboard , name = 'dashboard'),
path('category' , category_dashboard , name = 'category_dashboard'),
path('category/add-category' , add_category , name = 'add_category'),
path('category/edit-category/<int:id>/' , edit_category , name = 'edit_category'),
path('category/delete/<int:id>/' , delete_category , name = 'delete_category'),
] 
