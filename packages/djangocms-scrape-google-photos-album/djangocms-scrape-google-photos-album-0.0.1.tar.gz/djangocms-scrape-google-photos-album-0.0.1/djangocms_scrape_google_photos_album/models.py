from django.db import models
from cms.models import CMSPlugin


class GooglePhotosAlbumUrl(CMSPlugin):
    album_url = models.URLField()

    def __str__(self):
        return self.album_url
