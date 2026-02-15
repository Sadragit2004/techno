from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [

    path('blogs/',ShowBlogView.as_view(),name='blogs'),
    path('blog_detail/<str:slug>/',Blog_Detail.as_view(),name='blog_detail'),
    path('blogs_main/',Show_main_blog,name='main_blog')
]
