from django.shortcuts import render, get_object_or_404

from .models import Blog

def blog(request):
    blogs = Blog.objects
    paginate_by = 8
    return render(request, 'blog.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogdetail.html', {'detailblog': detailblog})