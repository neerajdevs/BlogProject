from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length= 100 , unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ('draft' , 'Draft'),
    ('publish' , 'Publish') 
)
class Blogs(models.Model):
    title = models.CharField(max_length=255 , unique=True)
    slug = models.SlugField(unique=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=500)
    description = models.TextField(max_length=5000)
    status = models.CharField(choices=STATUS_CHOICES , default='draft')
    is_featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title


