from django.db import models
from django.utils.translation import gettext_noop, gettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model


# Create your models here.
class Course(models.Model):
    title = models.CharField(_("Title"), max_length=500, blank=False)
    slug = models.SlugField(_('Slug'), allow_unicode=True, max_length=255, unique=True)
    abstract = models.CharField(_("Abstract"), max_length=2048, blank=True)
    description = models.TextField(verbose_name=_("Description"), blank=False)
    authors = models.ManyToManyField(get_user_model())
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    thumbnail = models.ImageField(_("Thumbnail"), upload_to="thumbnails/", null=True, blank=True)
    is_free = models.BooleanField(_("Is Free"), default=False)
    price = models.IntegerField(_("Price"), null=True, blank=True)
    time_duration = models.CharField(_("Time Duration"), blank=True, max_length=100)
    level = models.CharField(_("Level"), max_length=100, blank=True)
    key_point = models.TextField(_("Key Point"), blank=True)
    suggested_to = models.TextField(_("Suggested To"), blank=True)

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


class CourseSection(models.Model):
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=500, blank=False)


class CourseSectionItem(models.Model):
    VIDEO = 'video'
    ITEM_TYPE_CHOICE = (
        (VIDEO, _("Video"),),
    )
    section = models.ForeignKey(CourseSection, verbose_name=_("Course Sections"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=500, blank=False)
    item_type = models.CharField(_("Item Type"),max_length=255, choices=ITEM_TYPE_CHOICE, default=VIDEO)
    is_free = models.BooleanField(_("Is Free"), default=False)
    public_url = models.CharField(_("Public Url"),max_length=1024, blank=True)
    duration = models.CharField(_("Duration", ), max_length=128, blank=True)


