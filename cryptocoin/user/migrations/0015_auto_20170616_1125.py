# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20170616_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashes',
            old_name='points',
            new_name='value',
        ),
    ]
