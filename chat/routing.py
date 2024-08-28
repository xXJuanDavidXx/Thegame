from django.urls import path   
from .consumers import MyConsumer

websocket_urlpatterns = [
            path('ws/room/<room_id>/',MyConsumer.as_asgi()),
] 

