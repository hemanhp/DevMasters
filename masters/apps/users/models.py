from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _, gettext_noop
from django.db import models
import uuid


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(_("Bio"),max_length=500, blank=True)
    linkedin = models.CharField(_("Linkedin"), blank=True, max_length=255)
    twitter = models.CharField(_("Twitter"), blank=True, max_length=255)
    instagram = models.CharField(_("instagram"), blank=True, max_length=255)
    created = models.DateTimeField(_("Created"), auto_now_add=True, max_length=255)
    updated = models.DateTimeField(_("Updated"), auto_now=True, max_length=255)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profile')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
