# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_auto_20170416_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='page',
            field=models.ManyToManyField(related_name='sections', to='api.Page'),
        ),
    ]
