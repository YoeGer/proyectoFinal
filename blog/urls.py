from django.urls import path
from blog.views import *
 

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('post/', postFormulario, name='post'),
    path('leerPosts/', leerPosts, name='leerPosts'), 
    path('eliminarPost/<id>', eliminarPost, name='eliminarPost'), 
    path('editarPost/<id>', editarPost, name='editarPost'),
]