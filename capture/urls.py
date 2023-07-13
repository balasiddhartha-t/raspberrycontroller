from django.urls import path

from . import views

urlpatterns = [
    path("start", views.record, name="recordstart"),
    path("stop", views.stoprecord, name="stoprecord"),
]