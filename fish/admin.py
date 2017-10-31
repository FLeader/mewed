# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User,BulletIn
# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    pass

@admin.register(BulletIn)
class BulletIn(admin.ModelAdmin):
    pass


