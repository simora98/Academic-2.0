# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-26 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0003_auto_20190326_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='floated',
            field=models.BooleanField(default=False),
        ),
    ]
