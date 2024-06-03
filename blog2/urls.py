from django.urls import path
from .views import blog, blog_detail

urlpatterns = [
    path('blog.html/', blog, name='blog'),
    path('blog.html/<int:pk>/', blog_detail, name='blog_details'),
]
