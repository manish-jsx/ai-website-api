# image_processing/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import cv2

@api_view(['POST'])
def stitch_images(request):
    serializer = ImageUploadSerializer(data=request.data)
    if serializer.is_valid():
        person_image = cv2.imdecode(np.fromstring(request.FILES['person_image'].read(), np.uint8), cv2.IMREAD_COLOR)
        clothes_image = cv2.imdecode(np.fromstring(request.FILES['clothes_image'].read(), np.uint8), cv2.IMREAD_COLOR)

        # Resize clothes image to match person image size
        clothes_image_resized = cv2.resize(clothes_image, (person_image.shape[1], person_image.shape[0]))

        # Stitch images together
        stitched_image = cv2.addWeighted(person_image, 1, clothes_image_resized, 0.8, 0)

        # Save stitched image
        output_path = 'stitched_image.jpg'
        cv2.imwrite(output_path, stitched_image)

        return Response({'stitched_image_path': output_path}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
