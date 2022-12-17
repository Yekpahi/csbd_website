from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post, PostImage

# Create your views here.
def posts_list(request):

    posts = Post.objects.all()
    return render(request, 'post/posts_list.html', {
      'posts': posts
      })


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_images = PostImage.objects.filter(post=post)
    return render(request, 'post/post_details.html', {
        'post':post,
        'post_images':post_images
    })