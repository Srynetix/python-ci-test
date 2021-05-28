from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from web_project.portal.utils import get_or_create_ghost_user


class Note(models.Model):
    title = models.TextField(verbose_name=_("Note title"))
    content = models.TextField(verbose_name=_("Note content"))
    author = models.ForeignKey(
        verbose_name=_("Note author"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_or_create_ghost_user),
    )
    created_at = models.DateTimeField(
        verbose_name=_("Creation date"), auto_now_add=True
    )
    updated_at = models.DateTimeField(verbose_name=_("Last update date"), auto_now=True)
    tags = models.ManyToManyField(verbose_name=_("Tags"), to="portal.Tag")


class Tag(models.Model):
    name = models.CharField(verbose_name=_("Tag name"), max_length=255)
