from django.contrib import admin
from .models import *





class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_create', 'sum_of_photos', 'user',)
    ordering = ('date_of_create', 'sum_of_photos')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user', 'sum_of_photos', 'date_of_create']
        else:
            return []
admin.site.register(Album, AlbumAdmin)


class PhotosAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'date_of_create', 'photo',)
    search_fields = ('title',)
    readonly_fields = ['date_of_create']
    ordering = ('date_of_create', 'album')
    list_filter = ['album']

admin.site.register(Photos, PhotosAdmin)



class TagAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Tag, TagAdmin)

