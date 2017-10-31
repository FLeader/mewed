# coding: utf-8
from rest_framework import serializers
from .models import User, BulletIn

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'address')

class BulletInSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletIn
        fields = ('body','valid')
