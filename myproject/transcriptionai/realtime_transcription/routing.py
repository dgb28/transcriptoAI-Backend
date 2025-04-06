# your_project_name/routing.py
from django.urls import re_path
from transcriptionai.consumers import TranscriptionConsumer

websocket_urlpatterns = [
    re_path(r'ws/transcription/$', TranscriptionConsumer.as_asgi()),
]

# In your asgi.py, include the protocol type router:
from channels.routing import ProtocolTypeRouter, URLRouter
import django
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),
})
