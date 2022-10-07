from django.shortcuts import render
from blog.forms import *
from .models import *


def inicio(request):
    return render(request, 'blog/inicio.html')

def postFormulario(request):
    if request.method == "POST":
        form = PostForm(request.POST)
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