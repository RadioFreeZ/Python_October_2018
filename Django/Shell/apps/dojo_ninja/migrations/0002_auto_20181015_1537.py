# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='city',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dojo',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]
