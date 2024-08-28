from django.db import models   
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.


#Creación de salas para la comunicación
class Room(models.Model):      
    name = models.CharField(max_length=100, unique=True, verbose_name='nombre')
    users = models.ManyToManyField(User, related_name='rooms_joined', blank = True)
  
    def __str__(self):
        return self.name


