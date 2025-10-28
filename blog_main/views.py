from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .context_processors import *
from django.db.models import Q # Q object import karna zaroori hai

# Create your views here.

def blog(request):
    cate_obj = Category.objects.all()
    featured = Blogs.objects.filter(is_featured = True)
    Nonfeatured = Blogs.objects.filter(is_featured = False , status = 'publish')
    return render(request, 'home.html' , {'category'  : cate_obj , 'featured' : featured ,'Nonfeatured' : Nonfeatured  })

def filter_category(request , id):
    blogs = Blogs.objects.filter(category= id , status = 'publish')
    try:
         category = Category.objects.get(id = id)
    except :
        return HttpResponse("Category is not founds")
    
    # built in 404 error is category not found 
    # category = get_object_or_404(Category , id = id)

    return render(request , 'filteresPost.html' , {'posts' : blogs , 'category' : category} )

def search_blogs(request , slug):
    post = get_object_or_404(Blogs , slug = slug , status = 'publish')
    # category = Category.objects.all() # now it get by context [processors]
    return render(request , 'view_post.html' , {'blog' : post } )

def search(request):
    keyword = request.GET.get('keyword')  
    if keyword:
        # Q objects ka use karke 'OR' condition banao
        queryset = Blogs.objects.filter(
            Q(title__icontains=keyword) |       
            Q(author__username__icontains=keyword) , status = 'publish'  
        )
    else:
        # Agar koi keyword nahi hai, toh empty queryset ya saare blogs return kar sakte hain
        queryset = Blogs.objects.none() # Ya Blogs.objects.all() agar sab dikhane hain
    return render(request , 'search.html' , {'results' : queryset})