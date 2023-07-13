from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("record/start", views.record, name="recordstart"),
    path("record/stop", views.stoprecord, name="stoprecord"),
    path("command/<str:command>", views.command, name="command"),
]