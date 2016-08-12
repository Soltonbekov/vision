# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Advice(models.Model):
    frequency = models.IntegerField(u"Частота", default=0)
    category = models.CharField(u"Категория",max_length=45, blank=True, null=True, unique=True)
    text = models.TextField(u"Текст")

    class Meta:
        verbose_name = u"совет"
        verbose_name_plural = u"советы"

    def __unicode__(self):
        return "%s - %s" % (self.category, self.frequency)