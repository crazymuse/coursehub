# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-16 07:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20190416_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 7, 0, 59, 891916, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='likeactivity',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 7, 0, 59, 893443, tzinfo=utc)),
        ),
    ]