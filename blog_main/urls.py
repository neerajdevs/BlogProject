from django.urls import path
from .views import blog, filter_category, search_blogs

urlpatterns = [
    path("" , blog , name = "blog"),
    path("category/<int:id>/" , filter_category , name="filter_by_category"),
    path('<slug:slug>' , search_blogs , name = 'blogs')
]
