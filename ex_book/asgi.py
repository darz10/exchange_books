import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import exchange_chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ex_book.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            exchange_chat.routing.websocket_urlpatterns
        )
    ),
})