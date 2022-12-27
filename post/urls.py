from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.homepage, name = 'homepage'),
    path('post/<slug>/', views.post, name = 'post'),
    path('search/', views.search, name = 'search'),
    path('postlist/<slug>/', views.postlist, name = 'postlist'), 
    path('posts/', views.allposts, name = 'allposts'),
]