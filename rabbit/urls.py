from django.urls import path
from .views import HelloWorld
urlpatterns = [
    path('pushMessage', HelloWorld.as_view()),
]