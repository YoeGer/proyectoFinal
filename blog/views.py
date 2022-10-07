from django.shortcuts import render
from blog.forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def inicio(request):
    posts = Post.objects.all()
    return render(request, 'blog/inicio.html', {'posts': posts})

def postFormulario(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            titulo = informacion["titulo"]
            contenido = informacion["contenido"]
            imagen = informacion["imagen"]
            autor = informacion["autor"]
            fecha = informacion["fecha"]
            post = Post(titulo=informacion["titulo"], contenido=informacion["contenido"], imagen=informacion["imagen"], autor=informacion["autor"], fecha=informacion["fecha"])
            post.save() 
            return render(request, 'blog/inicio.html', {'mensaje': 'Articulo creado correctamente'})
    else: 
        form = PostForm() 
    return render(request, 'blog/postForm.html', {'formulario':form})

def leerPosts(request): 
    posts = Post.objects.all()
    return render(request, "blog/leerPosts.html", {'posts': posts})

def eliminarPost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    posts = Post.objects.all()
    return render (request, "blog/leerPosts.html", {"posts":posts})

def editarPost(request, id):
    post = Post.objects.get(id=id)
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid(): 
            informacion = form.cleaned_data
            titulo = informacion["titulo"]
            contenido = informacion["contenido"]
            imagen = informacion["imagen"]
            autor = informacion["autor"]
            fecha = informacion["fecha"]
            post.save()
            posts = Post.objects.all()
            return render (request, "blog/leerPosts.html", {'posts':posts})
    else: 
        form = PostForm(initial={"titulo":post.titulo, "contenido":post.contenido, "imagen":post.imagen, "autor":post.autor, "fecha":post.fecha})
        return render (request, "blog/editarPost.html", {"formulario":form, "post":post})

def postDetalle(request, id):
    post = Post.objects.get(id=id)
    return render (request, "blog/postDetalle.html", {'post':post})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usu = request.POST["username"]
            clave = request.POST["password"]
            usuario = authenticate(username=usu,password=clave)
            if usuario is not None:
                login(request,usurio)
                return render(request, "blog/inicio.html", {'mensaje':f'Bienvenido {usuario}'})
            else: 
                return render(request, "blog/login.html", {'formulario': form, 'mensaje':'Usuario o clave incorrecto'})
        else: 
            return render (request, "blog/login.html", {'formulario': form, 'mensaje':"Usuario o clave incorrecto"})
    else: 
        form = AuthenticationForm()
        return render (request, "blog/login.html", {'formulario':form})
    
