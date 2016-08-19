# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from fontawesome.fields import IconField


class Category(models.Model):
    """Categories"""
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    category_type = models.CharField(max_length=255)
    slug = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    icon = IconField()
    user = models.ForeignKey(User, verbose_name=u'Пользователь')


    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'категории'

    def __unicode__(self):
        return self.name
