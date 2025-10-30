from blog_main.models import Blogs
from django import forms


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'short_description', 'description', 'blog_image', 'category' , 'status']
