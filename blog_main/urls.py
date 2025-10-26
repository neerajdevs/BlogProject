from django.urls import path
from .views import blog, filter_category

urlpatterns = [
    path("" , blog , name = "blog"),
    path("category/<int:id>/" , filter_category , name="filter_by_category")
]
