import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter #Se debe importar
from channels.auth import AuthMiddlewareStack # se debe importar
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thegame.settings')


application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    "websocket": AuthMiddlewareStack(
    URLRouter( chat.routing.websocket_urlpatterns))

    })


