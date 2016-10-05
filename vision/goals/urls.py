# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from goals import views

urlpatterns =  [
    url(r'^$', views.goals, name='goals'),
    url(r'^new_goal/', views.new_goal, name='new_goal'),
]
