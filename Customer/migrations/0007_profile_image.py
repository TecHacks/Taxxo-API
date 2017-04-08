# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-06 19:11
from __future__ import unicode_literals

import Customer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0006_auto_20170227_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=3, upload_to=Customer.models.user_directory_path),
            preserve_default=False,
        ),
    ]
