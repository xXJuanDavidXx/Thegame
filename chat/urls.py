from django.urls import path   
from . import views            

urlpatterns = [
    path('', views.rooms,name="home"),
    path('room/<int:room_id>/', views.room, name="room"),
    path('create_room/', views.create_room, name='create_room'),
    path('request_to_join/<int:room_id>/', views.request_to_join, name='request_to_join'),
    path('manage_requests/<int:room_id>/', views.manage_requests, name='manage_requests'),
    path('mis_salas/',views.mis_salas, name="mis_salas")
    ]


