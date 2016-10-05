# -*- coding: utf-8 -*-

from django import forms
from goals.models import Goals


class NewGoal(forms.ModelForm):
    
    class Meta:
        model = Goals
        exclude = ( 'user', )
