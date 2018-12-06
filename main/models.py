from django.db import models

class Artist(models.Model):
     name =  models.CharField(max_length=200)
     photo_url = models.CharField(max_length=400, null=True, blank=True)
     nationality = models.CharField(max_length=255)

class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    preview_url = models.CharField(max_length=400)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')