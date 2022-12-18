from http.client import HTTPResponse
from .models import SubCategory, Category
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post, PostImage
import json
# Create your views here.
def posts_list(request):

    posts = Post.objects.all()
    return render(request, 'post/posts_list.html', {
      'posts': posts,
      })
def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HTTPResponse(json.dumps(result), content_type="application/json")

def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_images = PostImage.objects.filter(post=post)
    return render(request, 'post/post_details.html', {
        'post':post,
        'post_images':post_images
    })