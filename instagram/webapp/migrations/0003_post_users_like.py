# Generated by Django 2.1 on 2019-09-04 05:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]