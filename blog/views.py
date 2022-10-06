from django.shortcuts import render
from blog.forms import PostForm
from .models import Post


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
            post = PostForm(titulo=titulo, contenido=contenido, imagen=imagen, autor=autor, fecha=fecha)
            post.save() 
            return render(request, 'blog/inicio.html', {'mensaje': 'Articulo creado correctamente'})
    else: 
        form = PostForm() 
    return render(request, 'blog/postForm.html', {'formulario':form})
