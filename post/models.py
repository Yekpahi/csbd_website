from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    description = models.CharField(max_length=500, unique=True, verbose_name="Description")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, verbose_name="Contenu")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = models.FileField(blank=True)


    # On rajoute une classe Meta pour préciser notre modèle
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Post"
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    post_images = models.FileField(upload_to = 'post-images/')

    def __str__(self):
        return self.post.title