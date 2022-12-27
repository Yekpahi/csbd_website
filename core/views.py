from django.shortcuts import render
from .models import WelcomeMessage

def homepage(request):

    message = WelcomeMessage.objects.all()
    return render(request, 'core/home.html', {
      'message': message,
      })

def aboutpage(request):
    return render(request, 'core/about.html')

def contactpage(request):
    return render(request, 'core/contact.html')
