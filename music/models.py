
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    """Album model"""
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    """CASCADE, if the album is deleted the songs too"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

"""
album1.song_set.create(song_title="Blank space", file_type="mp3")

>>> from music.models import *
>>> Album.objects.all()
"""