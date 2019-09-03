from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='User'
    )

    avatar = models.ImageField(
        null=False,
        blank=False,
        upload_to='user_pics',
        verbose_name='Avatar'
    )

    about_me = models.TextField(
        null=True,
        blank=True,
        max_length=1000,
        verbose_name='About me'
    )

    phone_number = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        verbose_name='Phone number'
    )

    gender = models.CharField(
        null=True,
        blank=True,
        verbose_name='Gender',
        max_length=10,
    )

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
