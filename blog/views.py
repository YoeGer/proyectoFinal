from django.shortcuts import render
from blog.forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from blog.forms import UserEditForm

@login_required
def inicio(request):
    posts = Post.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)  
    return render(request, 'blog/inicio.html', {'posts': posts, 'avatar':obtenerAvatar(request)})

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
            return render(request, 'blog/inicio.html', {'mensaje': 'Articulo creado correctamente','avatar':obtenerAvatar(request)})
    else: 
        form = PostForm() 
    return render(request, 'blog/postForm.html', {'formulario':form})

@login_required
def leerPosts(request): 
    posts = Post.objects.all()
    return render(request, "blog/leerPosts.html", {'posts': posts,'avatar':obtenerAvatar(request)})

@login_required
def eliminarPost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    posts = Post.objects.all()
    return render (request, "blog/leerPosts.html", {"posts":posts,'avatar':obtenerAvatar(request)})

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
            return render (request, "blog/leerPosts.html", {'posts':posts, 'avatar':obtenerAvatar(request)})
    else: 
        form = PostForm(initial={"titulo":post.titulo, "contenido":post.contenido, "imagen":post.imagen, "autor":post.autor, "fecha":post.fecha})
        return render (request, "blog/editarPost.html", {"formulario":form, "post":post, 'avatar':obtenerAvatar(request)})

@login_required
def postDetalle(request, id):
    post = Post.objects.get(id=id)
    return render (request, "blog/postDetalle.html", {'post':post, 'avatar':obtenerAvatar(request)})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usu = request.POST["username"]
            clave = request.POST["password"]
            usuario = authenticate(username=usu,password=clave)
            if usuario is not None:
                login(request,usuario)
                return render(request, "blog/login.html", {'mensaje':f'Bienvenido {usuario}','avatar':obtenerAvatar(request)})
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
            return render(request, "blog/inicio.html", {'mensaje': f"Usuario {username} creado correctamente. Inicie sesion."})
        else: 
            return render(request, "blog/register.html", {'formulario': form, 'mensaje': "FORMULARIO INVALIDO"})
    else: 
        form = UserRegisterForm()
        return render (request, "blog/register.html", {'formulario': form})

@login_required
def editarPerfil(request): 
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info ["email"]
            usuario.password1 = info ["password1"]
            usuario.password2 = info ["password2"]
            usuario.first_name = info ["first_name"]
            usuario.last_name = info ["last_name"]
            usuario.save()
            return render (request, "blog/editarPerfil.html", {'mensaje':'Perfil editado correctamente','avatar':obtenerAvatar(request)})
        else: 
            return render (request, "blog/editarPerfil.html", {'formulario': form, 'usuario':usuario, 'mensaje':'FORMULARIO INVALIDO','avatar':obtenerAvatar(request)})
    else: 
        form = UserEditForm(instance=usuario)
    return render (request, "blog/editarPerfil.html", {'formulario':form, 'usuario':usuario})



@login_required
def agregarAvatar(request): 
    if request.method == "POST": 
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo = Avatar.objects.filter(user=request.user)
            if (len(avatarViejo)>0):
                avatarViejo[0].delete()
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, "blog/inicio.html", {'usuario':request.user, 'mensaje': 'Avatar agregado correctamente', 'imagen': avatar.imagen.url})
    else: 
        formulario = AvatarForm()
        return render (request, "blog/agregarAvatar.html", {'formulario':formulario, 'usuario': request.user})

def obtenerAvatar(request): 
    lista = Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen = lista[0].imagen.url
    else: 
        imagen = "/media/avatares/avatarPorDefecto/avatarPorDefecto.png"
    return imagen

@login_required
def sobreMi(request): 
    return render(request, "blog/sobreMi.html", {'avatar':obtenerAvatar(request)})