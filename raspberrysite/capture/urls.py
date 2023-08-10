from django.urls import path

from . import views

urlpatterns = [
    path("start", views.startrecord, name="recordstart"),
    path("stop", views.stoprecord, name="stoprecord"),
    path('video_stream', views.video_stream, name='video_stream'),
    path('video_stream_page/', views.video_stream_page, name='video_stream_page'),

]