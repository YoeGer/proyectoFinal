from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length = 250)
    contenido = RichTextUploadingField(blank=True, null=True)
    imagen = models.ImageField('imagen', upload_to = 'post/', null = True, blank = True )
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-fecha',)

    def __str__(self):
        return str(self.titulo) + ' | ' + str(self.autor)

 
