# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	full_name = models.CharField(max_length=500)
	profile_pic = models.FileField()
	github_link = models.CharField(max_length=2000)
	bio = models.TextField(max_length=2000)
	active = models.BooleanField(default=True)
	is_creator = models.BooleanField(default=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",primary_key=True)
	like_courses = models.ManyToManyField(User,related_name="like_users")

	def __str__(self):
		return self.full_name


class Course(models.Model):
	title = models.CharField(max_length=500)
	desc = models.TextField(max_length=2000)
	created_on = models.DateTimeField()
	publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name="published_courses")
	is_published = models.BooleanField(default=True)

	def __str__(self):
		return self.title


class Topic(models.Model):
	title = models.CharField(max_length=500)
	course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="topics")

	def __str__(self):
		return self.title


class SubTopic(models.Model):
	title = models.CharField(max_length=500)
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="subtopics")

	def __str__(self):
		return self.title

