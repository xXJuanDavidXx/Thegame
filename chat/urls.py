from django.urls import path   
from . import views            

urlpatterns = [
    path('', views.rooms,name="home"),
    path('room/<int:room_id>/', views.room, name="room"),
    
    ]


