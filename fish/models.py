# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

class BulletIn(models.Model):
    body = models.CharField(max_length=512)
    valid = models.CharField(max_length=32,default='valid')
