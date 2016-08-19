# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from income import views

urlpatterns =  [
    url(r'^$', views.wallets, name='wallets'),
    url(r'^create_trn/', views.create_trn, name='create_trn'),
]