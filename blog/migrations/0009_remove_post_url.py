# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-12-07 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201207_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]