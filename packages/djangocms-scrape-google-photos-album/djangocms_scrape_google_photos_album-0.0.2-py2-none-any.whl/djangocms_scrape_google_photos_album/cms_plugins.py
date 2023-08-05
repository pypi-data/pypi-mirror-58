import logging
import re

from cachetools import TTLCache
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
import requests

from . import models


logger = logging.getLogger(__name__)

# originally this was 139min chars. not actually sure the length they can be
REGEX = r"(https:\/\/lh3\.googleusercontent\.com\/[a-zA-Z0-9\-_]{128,})"
CACHE_TTL_IN_SECONDS = 60 * 30


def get_photos_from_html(html):
    # first and last elements are the album cover
    return re.findall(REGEX, html)[1:-1]


def get_photo_urls(album_url):
    logger.info('Scraping Google Photos album at: {}'.format(album_url))

    try:
        r = requests.get(album_url)

        photo_urls = get_photos_from_html(r.text) or []
        if not len(photo_urls):
            raise Exception('No photos found.')
        logger.info("# of images: {}".format(len(photo_urls)))

        photo_urls.reverse()  # makes the order appear the way it does on the website

        return photo_urls
    except Exception as err:
        logger.error('Google Photos scraping failed:\n{}'.format(str(err)))
    return []


CACHE = TTLCache(maxsize=1, ttl=CACHE_TTL_IN_SECONDS, missing=get_photo_urls)


class GooglePhotosAlbumPlugin(CMSPluginBase):
    model = models.GooglePhotosAlbumUrl
    name = _('Scrape Google Photos Public Album')
    module = _('Google')
    render_template = 'djangocms_scrape_google_photos_album/album.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super(GooglePhotosAlbumPlugin, self).render(
            context, instance, placeholder)
        context['photo_urls'] = CACHE[instance.album_url][::-1]
        return context


plugin_pool.register_plugin(GooglePhotosAlbumPlugin)
