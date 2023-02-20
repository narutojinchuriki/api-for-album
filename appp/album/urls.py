from django.urls import path, include, re_path

from .views import *

urlpatterns = [

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/album-list/', AlbumListApiView.as_view(), name='album-list'),
    path('api/v1/album-list/<int:pk>/', AlbumApiDetail.as_view(), name='album-detail'),
    path('api/v1/album-update/<int:pk>/', AlbumApiUpdate.as_view(), name='album-detail-update'),
    path('api/v1/album-delete/<int:pk>/', AlbumApiDelete.as_view(), name='album-detail-delete'),


    path('api/v1/photo-list/', PhotoListApiView.as_view(), name='photo-list'),
    path('api/v1/photo-list/<int:pk>/', PhotoApiDetail.as_view(), name='photo-detail'),
    path('api/v1/photo-update/<int:pk>/', PhotoApiUpdate.as_view(), name='photo-detail-update'),
    path('api/v1/photo-delete/<int:pk>/', PhotosApiDelete.as_view(), name='photo-detail-delete'),




]


