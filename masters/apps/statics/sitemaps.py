from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings


class StaticSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = settings.SITE_PROTOCOL

    def items(self):
        return ['home', 'about_us', 'contact_us', 'complaint']

    def location(self, item):
        return reverse(item)

