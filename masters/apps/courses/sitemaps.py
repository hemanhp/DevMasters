from django.contrib.sitemaps import Sitemap
from .models import Course, CourseSectionItem
from django.conf import settings


class CourseSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = settings.SITE_PROTOCOL

    def items(self):
        return Course.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated


class CourseLessonSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = settings.SITE_PROTOCOL

    def items(self):
        return CourseSectionItem.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated
