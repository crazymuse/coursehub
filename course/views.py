# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,ListView,DetailView,View,UpdateView,DeleteView
from models import Course,Topic, SubTopic, Profile,LikeActivity
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login,logout # For user auth
from django.contrib.auth.mixins import LoginRequiredMixin
from forms import UserForm
from django.contrib.auth import logout as django_logout
import json
from django.utils import timezone


# Create your views here.

class IndexView(LoginRequiredMixin,ListView):
    template_name = 'course/index.html'
    context_object_name='all_courses'    
    def get_queryset(self):
        return Course.objects.all()


class DetailView(LoginRequiredMixin,DetailView):
    model = Course
    template_name = 'course/detail.html'




def login_user(request): 
    if request.method=='POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        #Check if form is valid
        if user is not None:
             if user.is_active:
                 login(request,user)
                 return redirect('course:index')
        else:
            return render(request,'course/login_form.html',{'error_message':'User Credentials are not valid'})     

    return render(request,'course/login_form.html',{})



def logout(request):
    django_logout(request)
    return render(request, 'course/login_form.html')




class UserFormView(View):
    form_class = UserForm
    template_name = 'course/registration_form.html'
    
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        #Check if form is valid
        if form.is_valid():

             #REGISTRATION
             user = form.save(commit=False) # Getting a hold of the user
             # Clean the data 
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             print (username,password)
             user.set_password(password)
             user.save()
             # LOGIN
             user = authenticate(username=username,password=password)
             if user is not None:
                 if user.is_active:
                     login(request,user)
                     return redirect('course:index')

        return render(request, self.template_name, {'form':form})



class DeleteCourseView(DeleteView):
    model = Course
    




def editCourse(request,pk):
    if request.method == 'POST':
        # Need to add validation Test scenarios. What if the data is not 
        #proper
        course_data = json.loads(request.POST['course_data'])
        for topic_oid,topic_data in enumerate(course_data):
            print (topic_data['id'])
            tid = int(topic_data['id'].strip().split('-')[-1])
            topic = Topic.objects.get(pk=tid)
            topic.order_id=topic_oid
            if 'children' in  topic_data.keys():
                for subtopic_oid,subtopic_data in enumerate(topic_data['children']):
                    sid = int(subtopic_data['id'].strip().split('-')[-1])
                    subtopic = SubTopic.objects.get(pk=sid)
                    subtopic.order_id=subtopic_oid
                    subtopic.topic = topic
                    subtopic.save()
            topic.save()

    



    if not request.user.is_authenticated():
        return render(request, 'blog/login.html')
    else:
        template_name = "course/edit.html"
        context = {
            "course": Course.objects.get(pk=pk)
        }




        return render(request,template_name,context)


def addsubtractLikes(request,pk):
    if request.method == "POST":
        if 'change' in request.POST:
            change = int(request.POST['change'])
            if change == -1:
                LikeActivity.objects.filter(user_id=request.user.id).filter(course_id=pk).delete()
            else:
                print ('CHANGE = ',change)
                like = LikeActivity()
                like.user = request.user
                like.course = Course.objects.get(pk=pk)
                like.created = timezone.now()
                like.save()


    return render(request,"course/detail.html",{})
