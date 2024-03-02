from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('image_processing.urls')),  # Include the URLs of your myapi app
   
]

