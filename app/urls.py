from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('signup/',views.signup, name='signup'),
    path('categorias/', views.categorias, name='categorias'), 
    path('soporte/', views.soporte, name='soporte'), 
    path('help/', views.ayuda, name='ayuda'), 
#    path('me/', views.tu, name='tu'),






    #    path('about/',views.About.as_view()),
#    path('hola/<int:id>', views.my_view)


    ]




