# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms


class RegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'password', 'password_confirmation',
        )

    def clean(self):
        password = self.cleaned_data['password']
        password_confirmation = self.cleaned_data['password_confirmation']
        if password_confirmation != password:
            raise forms.ValidationError('Passwords doesn\'t match')
