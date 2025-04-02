from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import CommentForm, BlogForm

# Create your views here.
def home_page(request):
    bloglar = Blog.objects.all()
    if request.method == 'POST':
        qidiruv = request.POST.get('savol')
        bloglar = Blog.objects.filter(title__icontains=qidiruv)
    else:
        qidiruv = None

    context = {
        'blogs': bloglar
    }
    return render(request, 'blog.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = blog
            comment.save()
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'single.html', context)

def contact(request):
    return render(request, 'contact.html')

def add_blog(request):
     form = BlogForm
     context = {
         'form': form
     }
     return render(request, 'add_blog.html', context)

