from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm): 
    class Meta:
        model = Post
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese clave", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Confirme clave", widget = forms.PasswordInput)
    class Meta: 
            model = User
            fields = ['username', 'email', 'password1', 'password2']
            help_texts = {k:"" for k in fields}