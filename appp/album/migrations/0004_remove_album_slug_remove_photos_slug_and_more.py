# Generated by Django 4.1.5 on 2023-02-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_tag_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='slug',
        ),
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='tags',
            field=models.ManyToManyField(blank=True, editable=False, related_name='photos', to='album.tag'),
        ),
    ]