from django.shortcuts import render
from blog.forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def inicio(request):
    posts = Post.objects.all()
    return render(request, 'blog/inicio.html', {'posts': posts})

@login_required
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

@login_required
def leerPosts(request): 
    posts = Post.objects.all()
    return render(request, "blog/leerPosts.html", {'posts': posts})

@login_required
def eliminarPost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    posts = Post.objects.all()
    return render (request, "blog/leerPosts.html", {"posts":posts})

@login_required
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

@login_required
def postDetalle(request, id):
    post = Post.objects.get(id=id)
    return render (request, "blog/postDetalle.html", {'post':post})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usu = request.POST["username"]
            clave = request.POST["password"]
            usuario = authenticate(username=usu,password=clave)
            if usuario is not None:
                login(request,usuario)
                return render(request, "blog/inicio.html", {'mensaje':f'Bienvenido {usuario}'})
            else: 
                return render(request, "blog/login.html", {'formulario': form, 'mensaje':'Usuario o clave incorrecto'})
        else: 
            return render (request, "blog/login.html", {'formulario': form, 'mensaje':"Usuario o clave incorrecto"})
    else: 
        form = AuthenticationForm()
        return render (request, "blog/login.html", {'formulario':form})
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, "blog/inicio.html", {'mensaje': f"Usuario {username} creado correctamente"})
        else: 
            return render(request, "blog/register.html", {'formulario': form, 'mensaje': "FORMULARIO INVALIDO"})
    else: 
        form = UserRegisterForm()
        return render (request, "blog/register.html", {'formulario': form})
