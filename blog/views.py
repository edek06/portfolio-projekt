from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    posts = Blog.objects
    return render(request, 'blog/allblogs.html', {'posts':posts})

def blog_detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/blog_detail.html", {"detailblog":detailblog})