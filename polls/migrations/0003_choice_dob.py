# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 22:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160617_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
