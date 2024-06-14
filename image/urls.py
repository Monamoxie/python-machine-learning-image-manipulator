from django.contrib import admin
from django.urls import path
from django.urls import include
from image.views import ImageListView, ImageUploadView

urlpatterns = [
    path("", ImageListView.as_view(), name="index"),
    path("check", ImageUploadView.as_view(), name="check"),
]
