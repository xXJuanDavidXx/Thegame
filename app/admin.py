from django.contrib import admin
from .models import Consola, Juego, JuegoIndie, Profile


# Register your models here

admin.site.register(Juego)

admin.site.register(Consola)

admin.site.register(JuegoIndie)

admin.site.register(Profile)

