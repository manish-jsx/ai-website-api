# serializers.py in myapi

from rest_framework import serializers
from .models import APIRequest

class APIRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIRequest
        fields = '__all__'
