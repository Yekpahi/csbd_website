from django.contrib import admin
from .models import Post, PostImage

# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ("title", "status", "created_on", "last_updated")
    list_editable = ("status",)
    class Meta:
       model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass



