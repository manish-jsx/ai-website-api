# image_processing/serializers.py

from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    person_image = serializers.ImageField()
    clothes_image = serializers.ImageField()
