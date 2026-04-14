from django.shortcuts import render
from BlogApp.models import Categoria, Post

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    
    categorias = Categoria.objects.filter(post__in=posts).distinct()
    
    return render(request, "BlogApp/blog.html",{'posts':posts, 'categorias':categorias})

def categoria(request, categoria_id):
    
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    
    return render(request, "BlogApp/categorias.html", {'categoria':categoria, 'posts':posts})
