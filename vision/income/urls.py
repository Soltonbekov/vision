# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from income import views

urlpatterns =  [
    url(r'^$', views.wallets, name='wallets'),
    url(r'^new_wallet/', views.new_wallet, name='new_wallet'),
    url(r'^new_transaction/', views.new_transaction, name='new_transaction'),
    url(r'^create_trn/', views.create_trn, name='create_trn'),
]