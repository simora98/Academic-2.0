# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-11-08 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0008_auto_20191108_1850'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mtechcurriculum',
            unique_together=set([('batch', 'programme')]),
        ),
    ]
