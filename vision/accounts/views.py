# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect('/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    return render(request, 'accounts/login.html')


def signup(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.set_password(request.POST['password'])
        user.save()
        return redirect ('/')
    return render(request, 'accounts/signup.html', {'form': form})
