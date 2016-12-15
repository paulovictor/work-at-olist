# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaces', '0002_rename_level_to_mptt_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='marketplaces.Channel'),
        ),
    ]