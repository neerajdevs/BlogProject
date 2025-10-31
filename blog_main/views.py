from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .context_processors import *
from django.db.models import Q # Q object import karna zaroori hai

# Create your views here.

def blog(request):
    cate_obj = Category.objects.all()[:7]
    featured = Blogs.objects.filter(is_featured = True , status = 'publish')
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

def view_blogs(request , slug):
    post = Blogs.objects.filter(slug = slug , status = 'publish').first()
    comments = Comments.objects.filter(blogs = post).order_by('-created')
    comments_count = comments.count()
       
    if request.method == 'POST':
        if request.user.is_authenticated == True:
            comment_text = request.POST.get('comment_text')
            comment = Comments(user=request.user, blogs=post, comment=comment_text)
            comment.save()
            return HttpResponseRedirect(request.path_info)  # Page ko reload karne ke liye
        else:
            return redirect('login')  # User ko login page par redirect karne ke liye
    # category = Category.objects.all() # now it get by context [processors]
    return render(request , 'view_post.html' , {'blog' : post , 'comment' : comments , 'comments_count' : comments_count} )

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
