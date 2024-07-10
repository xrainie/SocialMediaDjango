from rest_framework import generics
from images.models import Image
from images.api.serializers import ImageSerializer
from rest_framework import viewsets


# class ImageListView(generics.ListAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer


# class ImageDetailView(generics.RetrieveAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer


class ImagesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer