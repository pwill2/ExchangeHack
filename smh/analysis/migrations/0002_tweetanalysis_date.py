# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 22:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetanalysis',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
