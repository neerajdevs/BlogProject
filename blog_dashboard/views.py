from django.shortcuts import render , redirect
from blog_main.models import Blogs , Category
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required as auth_required
from blog_main.context_processors import get_categories
from .form import CreateBlogForm
from django.utils.text import slugify
from django.contrib.auth.decorators import user_passes_test

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


def add_blog(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            if not blog.slug:
                blog.slug = slugify(blog.title)[:50]
            blog.save()
            return redirect('dashboard')
        else:
            print("Form errors:", form.errors)
    else:
        form = CreateBlogForm()
    return render(request, 'posts/add_blog.html', {'form': form, 'categories': categories})


def edit_blog(request,slug):
    blog = Blogs.objects.get(slug=slug)
    if request.method == 'POST':
        title = request.POST.get('title')
        short_description = request.POST.get('short_description')
        description = request.POST.get('description')
        status = request.POST.get('status')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        blog.title = title
        blog.short_description = short_description
        blog.description = description
        blog.status = status
        blog.category = category
        if 'slug' in request.POST :
            blog.slug = slugify(title)[:50]
        else:
            blog.slug = blog.slug
        blog.save()
        return redirect('dashboard')

    return render(request , "posts/edit_blog.html" , {'post' : blog} )

def delete_blog(request,id):
    blog = Blogs.objects.get(id=id)
    blog.delete()
    return redirect('dashboard')

# @user_passes_test(lambda u: u.is_superuser)
def user_view(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access denied.")
    users = User.objects.all()
    user_count = users.count()
    return render(request , 'users.html' , {'users' : users, 'user_count': user_count})