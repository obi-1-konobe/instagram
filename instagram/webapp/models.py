from django.conf import settings
from django.db.models import ImageField
from django.db import models


class Post(models.Model):
    picture = ImageField(
        null=True,
        blank=True,
        upload_to='user_pics',
        verbose_name='Picture'
    )

    description = models.TextField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Description',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='pictures',
        on_delete=models.PROTECT,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Add time')
