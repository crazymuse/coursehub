# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from course.models import Course,Topic,SubTopic,Profile,LikeActivity

# Register your models here.

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(Profile)
admin.site.register(LikeActivity)
