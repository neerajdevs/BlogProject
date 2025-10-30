from django.shortcuts import render , redirect
from blog_main.models import Blogs , Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required as auth_required
from blog_main.context_processors import get_categories

# Create your views here.
@auth_required(login_url='login')
def dashboard(request):
    blog_posts = Blogs.objects.all().order_by('created')
    total_count = blog_posts.count()
    category_count = Category.objects.count()
    return render(request , 'dashboard.html' , {'recent_posts' : blog_posts, 'total_posts' : total_count, 'total_categories' : category_count })

@auth_required(login_url='login')
def category_dashboard(request):
    categories = Category.objects.all().order_by('created')

    return render(request , "category.html" ,{'categories' : categories} )

def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        Category.objects.create(category_name = category_name)
    return render(request , "category.html" )

def edit_category(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        if category_name:
            category.category_name = category_name
            category.save()
            return redirect('category_dashboard')
        else:
            category.category_name = "Blogging"
            category.save()
            return redirect('category_dashboard')
        
    return render(request , "category/edit_category.html" , {'categories' : category})

def delete_category(request,id):
    
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category_dashboard')    
   