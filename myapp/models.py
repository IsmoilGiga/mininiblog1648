from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.URLField()

    def __str__(self):
        return self.title
    
    def comment_count(self):
        return Comment.objects.filter(blog_id=self).count()
    
    def get_all_comments(self):
        return Comment.objects.filter(blog_id=self)
    

class Comment(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=200)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class BlogLike(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'blog_id'], name='unique_user_blog_like')
        ]

    def __str__(self):
        return self.user_id + " " + self.blog_id


class CommentLike(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'comment_id'], name='unique_user_comment_like')
        ]

    def __str__(self):
        return self.user_id + " " + self.comment_id


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name