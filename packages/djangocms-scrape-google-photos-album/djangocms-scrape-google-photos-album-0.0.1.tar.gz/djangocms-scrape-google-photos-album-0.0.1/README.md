djangocms-scrape-google-photos-album
=====================================

**djangocms-scrape-google-photos-album** is a plugin for [django CMS](<http://django-cms.org>) that
allows you to include a public google photo album in your site by way of scraping their html.

---

**WARNING: This is implementation is likely to break due to the nature of scraping. The regex will
need to be updated whenever google changes the structure of that page.**

---


Requirements
------------
* python 3.5+
* django 1.11 (other versions may work, but this is the only one that has been tested)
* django-cms 3.5 (other versions may work, but this is the only one that has been tested)


Installation
------------
```
pip install djangocms-scrape-google-photos-album
```


Usage
-----

Note: Results are cached for **30 minutes**. If this doesn't serve your needs,
[make an issue](https://github.com/k-funk/djangocms-scrape-google-photos-album/issues/new).

#### `settings.py`:
```
INSTALLED_APPS = (
    ...
    'djangocms_scrape_google_photos_album',
    ....
)
```

[Override the template](https://docs.djangoproject.com/en/3.0/howto/overriding-templates/)
included, as it's likely to not be the html that you want. Below is an example of how you could use
it with [Bootstrap 3](https://getbootstrap.com/docs/3.3/) and
[featherlight.js](https://noelboss.github.io/featherlight/).

#### `/my_project/templates/djangocms_scrape_google_photos_album/album.html`
```
{% if photo_urls %}
  <div class="container-fluid">
    <div class="row" data-featherlight-gallery data-featherlight-filter="a" data-featherlight-type="image">
      {% for photo_url in photo_urls %}
        <div class="col-xs-6 col-sm-4 col-md-3">
          <a href="{{ photo_url }}=w1200-h1200">
            <img src="{{ photo_url }}=w300-h300-c" class="img-responsive" />
          </a>
        </div>
      {% endfor %}
    </div>
  </div>
{% endif %}
```
