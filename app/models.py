from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Consola(models.Model):
    consola = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='img/consolas', default='img/default_consola.jpg')

    def __str__(self):
        return self.consola

# Modelo Juego
class Juego(models.Model):
    titulo = models.CharField(max_length=20)
    caratula = models.ImageField(upload_to='img/caratula', default='default_image.jpg')   
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE) # esta viene a ser la llave foranea, no hace falta especificar mas porque djnago crea autamitacemnte el id 
    descripcion = models.CharField(max_length=200)                 #y automaticamente al pasarle la clase relaciona las tablas on_delete por si se elimina tambien lo haga su llave foranea
    Descarga = models.FileField(upload_to='Room/',default='archivos_juegos/default_file.txt') 
    
    def __str__(self):
        return self.titulo

# juegos indie

 ### class juegos_indie(models.Model) 
class JuegoIndie(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    desarrollador = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/indie', default='default_image.jpg')
    archivo = models.FileField(upload_to='archivos_juegos/',default='archivos_juegos/default_file.txt' )

    def __str__(self):
        return self.titulo


class JuegoIndieImagen(models.Model):
    juego = models.ForeignKey(JuegoIndie, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img/indie')

    def __str__(self):
        return f"Imagen de {self.juego.titulo}"
