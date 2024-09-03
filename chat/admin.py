from django.contrib import admin
from .models import Room, Mensajes

# Register your models here.

class AdminMensaje(admin.ModelAdmin):
    list_display = ('user', 'room', 'mensaje', 'tiempo')

    #Filtrar info 
    list_filter = ('room', 'user')



admin.site.register(Room)
admin.site.register(Mensajes,AdminMensaje)



