from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('categorias/', views.categorias, name='categorias'), 
    path('soporte/', views.soporte, name='soporte'), 
    path('help/', views.ayuda, name='ayuda'), 
    path('me/', views.tu, name='tu'),
    path('about/',views.about),
    path('hola/<str:username>', views.hola)
]




