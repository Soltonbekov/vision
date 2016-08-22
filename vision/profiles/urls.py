# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from profiles import views

urlpatterns =  [
    url(r'^$', views.profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
]
