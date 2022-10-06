from django.urls import path
from blog.views import postFormulario
from django.urls import path
from blog.views import * 

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('post/', postFormulario, name='post'),
]