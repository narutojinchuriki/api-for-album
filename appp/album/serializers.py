
from rest_framework import serializers
from .models import Album, Photos
class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Album
        #fields = ['title', 'content', 'category', 'is_published']
        fields = "__all__"

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['album', 'title', 'date_of_create', 'photo']
