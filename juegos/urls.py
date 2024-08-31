from django.urls import path
from . import views


urlpatterns = [
    path('SubirJuegoWeb/', views.subir_juego, name="subir"),
    path('JuegosWeb/', views.lista_juegos, name="listajuegos"),
    path('EjecutarJuego/<int:juego_id>', views.ejecutar_juego, name="ejecutar_juego"),
    
    ]
