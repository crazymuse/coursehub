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



# Create your views here.

class DetailView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'userprofile/detail.html'
