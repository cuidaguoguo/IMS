# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontIMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='ScoreId',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
