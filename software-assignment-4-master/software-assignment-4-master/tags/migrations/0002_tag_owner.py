# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 18:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='owner',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
