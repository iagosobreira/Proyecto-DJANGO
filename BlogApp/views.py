from django.shortcuts import render
from BlogApp.models import Categoria, Post

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request, "BlogApp/blog.html",{'posts':posts})
