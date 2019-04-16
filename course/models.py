# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import sys;
sys.path.append("..") #
from src import settings
from django.core.files.storage import FileSystemStorage


# Create your models here.

class BaseUser(models.Model):
	user = models.OneToOneField(User)

class Profile(models.Model):
	full_name = models.CharField(max_length=500,default="")
	profile_pic = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='logos', default='/logos/default_profile.jpg')
	github_link = models.CharField(max_length=2000,default="")
	bio = models.TextField(max_length=2000,default="")
	active = models.BooleanField(default=True)
	is_creator = models.BooleanField(default=False)
	profile_user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)

	def __str__(self):
		return self.profile_user.username


		

class Course(models.Model):
	title = models.CharField(max_length=500)
	desc = models.TextField(max_length=2000)
	created_on = models.DateTimeField(default=timezone.now())
	publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name="published_courses")
	is_published = models.BooleanField(default=True)
	course_pic = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='logos', default='/logos/defaultcourse.jpg')

	@property
	def sorted_topics(self):
	    return self.topics.order_by('order_id')

	@property
	def total_likes(self):
	    return self.likes.count()


	def __str__(self):
		return self.title


	def liked_by(self,userid):
		return self.likes.filter(user_id==userid).count()


	def get_likes_url(self):
 		return reverse('course:likeschange', kwargs={'pk': self.pk});

	def get_edit_url(self):
 		return reverse('course:edit', kwargs={'pk': self.pk});

 	def get_subtopics_count(self):
 		count = 0;
 		for topic in self.topics.all():
 			count+=topic.subtopics.count()

 		return count;



#	@property
#	def likes_course(self,course_id):
#	    return self.likes.objects.filter(course.id=)


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
    user = models.ForeignKey(User,related_name='likes')
    course = models.ForeignKey(Course,related_name='likes')
    created = models.DateTimeField(default=timezone.now())

    class Meta:
        unique_together = ('user', 'course',)


    #@staticmethod
    #def has_liked(userid,courseid):
    #	return LikeActivity.objects.filter(user_id=userid).filter(course_id=courseid).count()


    def __str__(self):
        return self.user.username + "  likes  '" + self.course.title +"'"

        


