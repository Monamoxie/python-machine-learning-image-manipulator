from django.contrib import admin
from django.urls import path
from django.urls import include
from image.views import ImageListView

urlpatterns = [
    path("", ImageListView.as_view(), name="index"),
]
