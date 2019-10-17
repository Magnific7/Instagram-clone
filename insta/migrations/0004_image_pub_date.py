# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-17 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
