from django.contrib import admin
from .models import Blog, Comment, BlogLike, CommentLike

# Register your models here.

admin.site.register(BlogLike)
admin.site.register(CommentLike)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'image')
    search_fields = ('title', 'author__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'name', 'blog_id', 'created_at')
    search_fields = ('text', 'name', 'blog_id__title')
    