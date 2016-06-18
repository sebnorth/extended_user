# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import polls.generator


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_choice_rumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='rumber',
            field=models.IntegerField(default=polls.generator.randomf),
        ),
    ]