# -*- coding: utf-8 -*-

from django import forms
from profiles.models import Profile


class EditProfile(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ( 'user', )
