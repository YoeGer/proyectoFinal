from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class PostForm(ModelForm): 
    class Meta:
        model = Post
        fields = '__all__'


