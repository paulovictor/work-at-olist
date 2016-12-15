# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaces', '0003_change_related_name_of_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='marketplaces.Channel'),
            preserve_default=False,
        ),
    ]
