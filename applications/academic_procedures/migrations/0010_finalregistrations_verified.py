# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-28 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_procedures', '0009_auto_20190327_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalregistrations',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
