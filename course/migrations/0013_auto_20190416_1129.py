# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-16 11:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20190416_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 11, 29, 40, 549119, tzinfo=utc)),
        ),
    ]