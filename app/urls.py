from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('signup/',views.signup, name='signup'),
    path('login/',views.registro, name='login'),
    path('logout',views.singout, name='logout'),
    path('me/', views.tu, name='tu'),
    path('edit/', views.editar, name="edit"),
    path('upload/',views.indie, name='upload'),
    path('mis-juegos/', views.mis_juegos, name='mis_juegos'),
    path('indie/', views.lista_indie, name='indie'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/consola/<int:consola_id>/', views.juegos_por_consola, name='juegos_por_consola'),
    path('soporte/', views.soporte, name='soporte'), 
    path('help/', views.ayuda, name='ayuda'), 
    path('buscar/', views.search_view, name='search_view'),
    

    #    path('about/',views.About.as_view()),
#    path('hola/<int:id>', views.my_view)


    ]




