from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return render(request, "ProyectoDjangoApp/home.html")

def servicios(request):
    
    return render(request, "ProyectoDjangoApp/servicios.html")

def tienda(request):
    
    return render(request, "ProyectoDjangoApp/tienda.html")

def blog(request):
    
    return render(request, "ProyectoDjangoApp/blog.html")
