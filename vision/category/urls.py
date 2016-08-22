# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from category import views

urlpatterns =  [
    url(r'^$', views.categories, name='categories'),
    url(r'^new_category/', views.new_category, name='new_category'),
]
