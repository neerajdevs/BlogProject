from django.urls import path
from .views import *

urlpatterns = [
path('' , dashboard , name = 'dashboard'),
path('category' , category_dashboard , name = 'category_dashboard'),
path('category/add-category' , add_category , name = 'add_category'),
path('category/edit-category/<int:id>/' , edit_category , name = 'edit_category'),
path('category/delete/<int:id>/' , delete_category , name = 'delete_category'),
path('posts/add-blog',add_blog , name = 'add_blog'),
path('posts/edit-blog/<slug:slug>/',edit_blog , name = 'edit_blog'),
path('posts/delete-blog/<int:id>/',delete_blog , name = 'delete_blog'),
path('users' , user_view , name = 'user_view'),
] 
