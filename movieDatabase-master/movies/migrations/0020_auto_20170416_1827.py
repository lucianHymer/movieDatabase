# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-16 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_auto_20170415_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tag',
            field=models.ManyToManyField(blank=True, to='movies.Tag'),
        ),
    ]
