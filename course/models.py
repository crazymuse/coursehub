# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Course(models.Model):
	title = models.CharField(max_length=500)
	desc = models.TextField(max_length=2000)
	created_on = models.DateTimeField()
	publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name="published_courses")
	is_published = models.BooleanField(default=True)

	@property
	def sorted_topics(self):
	    return self.topics.order_by('order_id')

	@property
	def total_likes(self):
	    return self.likes.count()


	def __str__(self):
		return self.title

class Profile(models.Model):
	full_name = models.CharField(max_length=500)
	profile_pic = models.FileField()
	github_link = models.CharField(max_length=2000)
	bio = models.TextField(max_length=2000)
	active = models.BooleanField(default=True)
	is_creator = models.BooleanField(default=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",primary_key=True)

	def __str__(self):
		return self.full_name


class Topic(models.Model):
	title = models.CharField(max_length=500)
	course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="topics")
	order_id=models.IntegerField(default=0)

	@property
	def sorted_subtopics(self):
	    return self.subtopics.order_by('order_id')


	def __str__(self):
		return self.title


class SubTopic(models.Model):
	title = models.CharField(max_length=500)
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="subtopics")
	order_id=models.IntegerField(default=0)

	def __str__(self):
		return self.title


class LikeActivity(models.Model):
    user = models.ForeignKey(Profile,related_name='likes', unique=True )
    course = models.ForeignKey(Course,related_name='likes')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.user.username + "  	likes  '" + self.course.title +"'"
