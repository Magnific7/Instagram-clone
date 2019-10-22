# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-22 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='image_likes',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='comment',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]