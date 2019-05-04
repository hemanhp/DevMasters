from django.db import models
from django.utils.translation import gettext_noop, gettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model


# Create your models here.
# class Author(models.Model):
#     full_name = models.CharField(_("Full Name "), max_length=500, blank=False)
#     slug = models.SlugField(_('Slug'), allow_unicode=True, max_length=255, unique=True)
#     bio = models.TextField(_("Bio"), blank=True)
#
#     linkedin = models.CharField(_("Linkedin"), blank=True, max_length=255)
#     twitter = models.CharField(_("Twitter"), blank=True, max_length=255)
#     instagram = models.CharField(_("instagram"), blank=True, max_length=255)
#     created = models.DateTimeField(_("Created"), auto_now_add=True)
#     updated = models.DateTimeField(_("Updated"), auto_now=True)
#
#     def __str__(self):
#         return self.full_name
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             suffix = 0
#             potential = base = slugify(self.full_name[:255])
#             while not self.slug:
#                 if suffix:
#                     potential = "%s-%s" % (base, suffix)
#                 if not Author.objects.filter(slug=potential).exists():
#                     self.slug = potential
#                 suffix += 1
#
#         super(Author, self).save(*args, **kwargs)
#
#     class Meta:
#         ordering = ['-created']
#         verbose_name = _("Author")
#         verbose_name_plural = _("Authors")


class Course(models.Model):
    title = models.CharField(_("Title"), max_length=500, blank=False)
    slug = models.SlugField(_('Slug'), allow_unicode=True, max_length=255, unique=True)
    description = models.TextField(verbose_name=_("Description"), blank=False)
    authors = models.ManyToManyField(get_user_model())
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            suffix = 0
            potential = base = slugify(self.title[:255])
            while not self.slug:
                if suffix:
                    potential = "%s-%s" % (base, suffix)
                if not Course.objects.filter(slug=potential).exists():
                    self.slug = potential
                suffix += 1

        super(Course, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
