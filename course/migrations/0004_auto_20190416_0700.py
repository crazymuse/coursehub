# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-16 07:00
from __future__ import unicode_literals

import datetime
import django.core.files.storage
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20190416_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_pic',
            field=models.FileField(default='/home/jaley/coursehub/medialogos/defaultcourse.jpg', storage=django.core.files.storage.FileSystemStorage(location=b'/home/jaley/coursehub/media'), upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 7, 0, 54, 437027, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='likeactivity',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 7, 0, 54, 438600, tzinfo=utc)),
        ),
    ]
