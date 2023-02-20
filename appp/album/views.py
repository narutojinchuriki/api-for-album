from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .models import Album, Photos
from .serializers import AlbumSerializer, PhotosSerializer




class AlbumListApiView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AlbumApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsOwnerOrReadOnly]


class AlbumApiDelete(generics.RetrieveDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAdminOrReadOnly]


class AlbumApiDetail(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsOwnerOrReadOnly]

######

class PhotoListApiView(generics.ListCreateAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class PhotoApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class PhotosApiDelete(generics.RetrieveDestroyAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    permission_classes = [IsAdminOrReadOnly]



class PhotoApiDetail(generics.RetrieveAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    permission_classes = [IsOwnerOrReadOnly]






