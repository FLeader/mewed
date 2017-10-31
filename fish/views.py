# coding: utf-8
from __future__ import unicode_literals

from django.shortcuts import render

import django_filters
from rest_framework import viewsets,filters

from .models import User,BulletIn
from .serializer import UserSerializer,BulletInSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BulletInViewSet(viewsets.ModelViewSet):
    queryset = BulletIn.objects.all()
    serializer_class = BulletInSerializer
