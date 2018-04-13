#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True, null=True) #black是django admin里可以为空,null是表里可以为空
    content = models.TextField()
    author = models.ForeignKey("BBS_User")
    view_cnt = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Comments(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

class BBS_User(models.Model):
    #user = models.ForeignKey(User)  #一对多
    user = models.OneToOneField(User)   #一对一
    signature = models.CharField(max_length=128, default='this guy is too lazy')
    photo = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/1.jpg")

    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name
