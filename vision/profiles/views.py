# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from profiles.models import Profile
from profiles.forms import EditProfile


def profile(request):
    profile, created = Profile.objects.get_or_create(user = request.user)
    return render(request,'profiles/profile.html', {'profile': profile})


def edit_profile(request):
    form = EditProfile(request.POST or None, instance = Profile.objects.get(user = request.user))
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect ('/')
    return render(request, 'profiles/edit_profile.html', {'form': form})
