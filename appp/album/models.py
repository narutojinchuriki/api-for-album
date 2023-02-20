from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, auto_created=True)
    title = models.CharField(max_length=150, db_index=True)
    date_of_create = models.DateTimeField(auto_now_add=True)      # non-edit
    sum_of_photos = models.IntegerField(default=0)           # non-edit

    def __str__(self):
        return self.title


class Photos(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True)
    date_of_create = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    photo = models.ForeignKey('Photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title











