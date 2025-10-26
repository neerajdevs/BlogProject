from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def blog(request):
    cate_obj = Category.objects.all()
    featured = Blogs.objects.filter(is_featured = True)
    Nonfeatured = Blogs.objects.filter(is_featured = False , status = 'publish')
    return render(request, 'home.html' , {'category'  : cate_obj , 'featured' : featured ,'Nonfeatured' : Nonfeatured  })

def filter_category(request , id):
    blogs = Blogs.objects.filter(category= id , status = 'publish')
    print(blogs)
    return render(request , 'filteresPost.html' , {'posts' : blogs} )
