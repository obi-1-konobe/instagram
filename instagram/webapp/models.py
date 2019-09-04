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


class Comment(models.Model):
    post = models.ForeignKey(
        'webapp.Post',
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Post'
    )

    author = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Author'
    )

    text = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name='Text'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Add time'
    )

    def __str__(self):
        return self.text[:20]