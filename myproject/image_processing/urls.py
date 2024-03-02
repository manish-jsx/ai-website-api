# image_processing/urls.py

from django.urls import path
from .views import stitch_images

urlpatterns = [
    path('stitch/', stitch_images, name='stitch_images'),
]
