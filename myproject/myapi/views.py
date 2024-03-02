from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer  # Import JSONRenderer
from .models import APIRequest

class APIRequestView(APIView):
    renderer_classes = [JSONRenderer]
    
    def post(self, request):
        # Implement your pricing logic here
        # For demonstration purposes, let's assume every request is allowed
        APIRequest.objects.create(user=request.user)
        return Response({'message': 'API request successful'}, status=status.HTTP_200_OK)
    
    def get(self, request):
        # Implement logic for GET requests if needed
        return Response({'message': 'GET request received'}, status=status.HTTP_200_OK)
