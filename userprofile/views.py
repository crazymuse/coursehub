# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from course.models import Profile

# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,ListView,DetailView,View,UpdateView,DeleteView
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login,logout # For user auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def detailView(request,pk):
	print (type(pk))
	print (type(request.user.id))
	profile_list = Profile.objects.filter(profile_user_id=pk)
	# Do not allow other people to view your profile
	if (len(profile_list) == 0) or (int(pk) != int(request.user.id)) :
		return redirect('course:index')
	else:
		return render(request,'userprofile/detail.html',context={'profile':profile_list[0]})

