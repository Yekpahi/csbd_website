from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class WelcomeMessage(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True),
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    welcomeImage = models.ImageField(null=True, upload_to='welcome_image')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title