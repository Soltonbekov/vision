# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from category.models import Category
from category.forms import NewCategory


def categories(request):
    categories = Category.objects.filter(user = request.user)
    return render(request,'category/categories.html', {'categories': categories})


def new_category(request):
    form = NewCategory(request.POST or None)
    if form.is_valid():
        category = form.save(commit=False)
        category.user = request.user
        category.save()
        return redirect ('/')
    return render(request, 'category/new_category.html', {'form': form})
