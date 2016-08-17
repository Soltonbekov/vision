# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from fontawesome.fields import IconField


class Wallets(models.Model):
    """User wallets"""
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    icon = IconField()
    user = models.ForeignKey(User, verbose_name=u'Пользователь')

    class Meta:
        verbose_name = u'кошелек'
        verbose_name_plural = u'кошельки'

    def __unicode__(self):
        return self.name

    def update_wallet_balance(self, amount):
        self.available_balance += amount


class Transactions(models.Model):
    """Transaction class"""
    desc = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=3)
    value_date = models.DateTimeField(auto_now_add=True)
    drcr_ind = models.CharField(max_length=1)
    wallet = models.ForeignKey(Wallets)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = u'проводка'
        verbose_name_plural = u'проводки'

    def __unicode__(self):
        return self.desc


class Income(models.Model):
    """Regular Income transactions"""
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=100, default='Salary')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    period = models.CharField(max_length=100, default='Monthly')
    icon = IconField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'регулярный доход'
        verbose_name_plural = u'регулярные доходы'

    def __unicode__(self):
        return self.name


class Outcome(models.Model):
    """Regular Outcome transactions"""
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    name = models.CharField(max_length=255)
    destination = models.CharField(max_length=100, default='Bills')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    period = models.CharField(max_length=100, default='Monthly')
    icon = IconField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'регулярный расход'
        verbose_name_plural = u'регулярные расходы'

    def __unicode__(self):
        return self.name
