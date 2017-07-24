# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid

# Create your models here.
class UserModel(models.Model):

    name = models.CharField(max_length=120)

    email = models.EmailField()

    username = models.CharField(max_length=120)

    password = models.CharField(max_length=40)

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

class SessionToken(models.Model):

    user = models.ForeignKey(UserModel)

    session_token = models.CharField(max_length=255)

    created_on = models.DateTimeField(auto_now_add=True)

    is_valid = models.BooleanField(default=True)

    def create_token(self):

        self.session_token = uuid.uuid4()

class PostModel(models.Model):

    user = models.ForeignKey(UserModel)

    image = models.FileField(upload_to = 'user_images')

    image_url = models.CharField(max_length=255)

    caption = models.CharField(max_length=255)

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    def like_count(self):
        return len(LikeModel.objects.filter(post=self))


class LikeModel(models.Model):

    user = models.ForeignKey(UserModel)

    post = models.ForeignKey(PostModel)

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

