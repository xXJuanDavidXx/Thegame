from django.db import models
from django.contrib.auth.models import User


class GamesWeb(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo_js = models.FileField(upload_to='juegos/')
    imagen = models.ImageField(upload_to='juegos_imagenes/', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre




