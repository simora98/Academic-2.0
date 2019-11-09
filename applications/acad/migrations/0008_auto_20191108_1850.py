# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-11-08 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0007_curriculumcourse_mtech_semester'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='batchsemester',
            unique_together=set([('batch', 'semester', 'programme')]),
        ),
        migrations.AlterUniqueTogether(
            name='mtechsemester',
            unique_together=set([('batch', 'semester', 'programme')]),
        ),
    ]
