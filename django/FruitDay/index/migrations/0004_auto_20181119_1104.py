# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-19 03:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20181119_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='spce',
            new_name='spec',
        ),
    ]