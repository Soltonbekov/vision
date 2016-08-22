# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from notification.models import Advice
from django.contrib.auth.decorators import login_required

def advice_of_day(request):
    advice = Advice.objects.order_by('?').first
    context = {
        'advice': advice,
    }
    return render(request, 'notification/advice.html', context)
