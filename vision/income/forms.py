# -*- coding: utf-8 -*-

from django import forms
from income.models import Wallets, Transactions, Income, Outcome
from category.models import Category


class NewWallet(forms.ModelForm):
    
    class Meta:
        model = Wallets
        exclude = ( 'user', )


class NewTransaction(forms.ModelForm):
    
    class Meta:
        model = Transactions
        exclude = ( 'user', )


# class NewExpensesCategory(forms.ModelForm):
    
#     class Meta:
#         model = Income
#         exclude = ( 'user', )


# class NewIncomeCategory(forms.ModelForm):
    
#     class Meta:
#         model = Outcome
#         exclude = ( 'user', )
