# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,ListView,DetailView,View
from models import Course,Topic, SubTopic
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login,logout # For user auth
from django.contrib.auth.mixins import LoginRequiredMixin
from forms import UserForm


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
    logout(request)
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
             user.set_password(password)
             user.save()

             # LOGIN
             user = authenticate(username=username,password=password)
             if user is not None:
                 if user.is_active:
                     login(request,user)
                     return redirect('course:index')

        return render(request, self.template_name, {'form':form})

