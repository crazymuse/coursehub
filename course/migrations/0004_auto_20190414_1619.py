# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-14 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20190414_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]