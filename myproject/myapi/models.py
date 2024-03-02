# models.py in myapi

from django.db import models
from django.contrib.auth.models import User

class APIRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)
