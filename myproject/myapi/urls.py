# urls.py in myapi

from django.urls import path
from . import views

urlpatterns = [
    path('api-request/', views.APIRequestView.as_view(), name='api-request'),
]

