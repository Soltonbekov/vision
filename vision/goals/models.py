# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from fontawesome.fields import IconField


class Goals(models.Model):
    """User goals"""
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    picture = models.ImageField(u'Фотография пользователя', upload_to='profiles/upload/goals_pic/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    icon = IconField()
    user = models.ForeignKey(User, verbose_name=u'Пользователь')

    class Meta:
        verbose_name = u'цель'
        verbose_name_plural = u'цели'

    def __unicode__(self):
        return self.name
