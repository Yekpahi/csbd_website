from django.shortcuts import render
from .models import WelcomeMessage
from post.models import Post
from post.models import PostImage

def homepage(request):

    message = WelcomeMessage.objects.all()
    posts = Post.objects.all()
    return render(request, 'core/home.html', {
      'message': message,
      'posts': posts
      })

def aboutpage(request):
    return render(request, 'core/about.html')

def contactpage(request):
    return render(request, 'core/contact.html')
