# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_choice_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='rumber',
            field=models.IntegerField(default=2),
        ),
    ]