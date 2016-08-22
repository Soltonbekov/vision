# -*- coding: utf-8 -*-

from django import forms
from category.models import Category


class NewCategory(forms.ModelForm):
    
    class Meta:
        model = Category
        exclude = ( 'user', )
