"""
ASGI config for rabbitMq_django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import rabbit.routing  # ← This must point to your app's routing file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbitMq_django.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            rabbit.routing.websocket_urlpatterns  # ← should be defined
        )
    ),
})

