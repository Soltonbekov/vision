# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from notification import views

#from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^wallets/', include('income.urls')),
    url(r'^$', views.advice_of_day, name='advice_of_day'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
