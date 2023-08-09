from django.urls import path

from . import views

urlpatterns = [
    path("start", views.startrecord, name="recordstart"),
    path("stop", views.stoprecord, name="stoprecord"),
]