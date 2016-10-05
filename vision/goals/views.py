# -*- coding: utf-8 -*-

import decimal

from datetime import datetime
from django.shortcuts import render, redirect
from goals.models import Goals
from goals.forms import NewGoal


def goals(request):
    goals = Goals.objects.filter(user = request.user)
    return render(request,'goals/goals.html', {'goals': goals})


def new_goal(request):
    form = NewGoal(request.POST or None)
    if form.is_valid():
        goal = form.save(commit=False)
        goal.user = request.user
        goal.save()
        return redirect ('/')
    return render(request, 'goals/new_goal.html', {'form': form})
