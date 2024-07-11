from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Consola(models.Model):
    consola = models.CharField(max_length=50)

    def __str__(self):
        return self.consola

# Modelo Juego
class Juego(models.Model):
    titulo = models.CharField(max_length=20)
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE) # esta viene a ser la llave foranea, no hace falta especificar mas porque djnago crea autamitacemnte el id 
    descripcion = models.CharField(max_length=200)                 #y automaticamente al pasarle la clase relaciona las tablas on_delete por si se elimina tambien lo haga su llave foranea
    Descarga = models.URLField(max_length=200, null=True) 
    
    def __str__(self):
        return self.titulo

# juegos indie

class Usuario_Desarollador(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()


    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


    def __str__(self):
        return self.nombre



 ### class juegos_indie(models.Model) 
class JuegoIndie(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    desarrollador = models.ForeignKey(Usuario_Desarollador, on_delete=models.CASCADE, related_name='juegos')

    def __str__(self):
        return self.titulo



