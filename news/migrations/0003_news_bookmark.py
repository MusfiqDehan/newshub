# Generated by Django 3.2 on 2021-05-07 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]
