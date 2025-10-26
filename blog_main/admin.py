from django.contrib import admin
from .models import Category , Blogs
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'category_name' , 'created' , 'updated']
admin.site.register(Category , CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'category' , 'created' , 'updated']
    prepopulated_fields = {'slug' : ('title',)}
    search_fields = ['id' , 'title' , 'author__username' , 'category__category_name']
admin.site.register(Blogs , BlogAdmin)