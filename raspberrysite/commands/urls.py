from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("command/<str:command>", views.command, name="command"),
]