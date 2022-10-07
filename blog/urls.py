from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView
 

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('post/', postFormulario, name='post'),
    path('leerPosts/', leerPosts, name='leerPosts'), 
    path('eliminarPost/<id>', eliminarPost, name='eliminarPost'), 
    path('editarPost/<id>', editarPost, name='editarPost'),
    path('postDetalle/<id>', postDetalle, name='postDetalle'),
    path('login/', login_request, name='login'), 
    path('register/', register, name='register'), 
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name = 'logout'), 
    path('editarPerfil/', editarPerfil, name='editarPerfil'), 
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
]