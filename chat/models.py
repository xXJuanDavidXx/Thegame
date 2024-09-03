from django.db import models   
from django.contrib.auth.models import User


# Create your models here.


#Creación de salas para la comunicación
class Room(models.Model):      
    name = models.CharField(max_length=100, unique=True, verbose_name='nombre')
    img = models.ImageField(upload_to='salas', default='default_image.jpg')
    users = models.ManyToManyField(User, related_name='rooms_joined', blank = True)
    creador = models.ForeignKey(User, related_name='created_rooms', on_delete=models.CASCADE)
    pendientes = models.ManyToManyField(User, related_name='pending_rooms', blank=True)


    def __str__(self):
        return self.name


##Persistencia de los mensajes 
class Mensajes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='sala')
    mensaje = models.TextField(verbose_name="Mensaje")
    tiempo = models.DateTimeField(auto_now_add=True, verbose_name='Enviado')

    def __str__(self):
        return self.mensaje










