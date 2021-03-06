# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-13 02:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('desc', models.TextField(max_length=2000)),
                ('created_on', models.DateTimeField()),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('full_name', models.CharField(max_length=500)),
                ('profile_pic', models.FileField(upload_to=b'')),
                ('github_link', models.CharField(max_length=2000)),
                ('bio', models.TextField(max_length=2000)),
                ('active', models.BooleanField(default=True)),
                ('is_creator', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('like_courses', models.ManyToManyField(related_name='like_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtopics', to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='course.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
