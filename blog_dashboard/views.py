from django.shortcuts import render
from blog_main.models import Blogs , Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required as auth_required

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