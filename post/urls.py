from django.urls import path 
from .import views

urlpatterns = [
    path('posts-list/', views.posts_list, name = 'posts'),
    path('<slug:slug>/', views.post_details, name='post_details'),
]
