# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170416_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, help_text='Only visible to you. Use it to manage your footers', max_length=255, null=True)),
                ('copyrightText', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Copyright text')),
            ],
        ),
        migrations.RemoveField(
            model_name='pagelink',
            name='page',
        ),
        migrations.AddField(
            model_name='page',
            name='showInFooter',
            field=models.BooleanField(default=True, verbose_name='Show in footer'),
        ),
        migrations.AddField(
            model_name='page',
            name='showInNavigation',
            field=models.BooleanField(default=True, verbose_name='Show in navigation (toolbar and sidenav)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, default=None, help_text='Only visible to you. Use it to manage your sections', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='toolbar',
            name='name',
            field=models.CharField(blank=True, default=None, help_text='Only visible to you. Use it to manage your toolbars', max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='PageLink',
        ),
    ]
