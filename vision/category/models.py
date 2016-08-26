# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from fontawesome.fields import IconField



class Category(models.Model):
    """Categories"""
    CATEGORY_TYPE_CHOICES = (
        (u'I', u'Income'),
        (u'E', u'Expenses'),
    )

    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPE_CHOICES, blank=True, null=True)
    slug = models.CharField(max_length=45, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    icon = IconField()
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    parent_category = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'категории'

    def __unicode__(self):
        return self.name
