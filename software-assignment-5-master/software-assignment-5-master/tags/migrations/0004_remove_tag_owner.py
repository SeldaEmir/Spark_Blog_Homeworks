# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20161220_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='owner',
        ),
    ]
