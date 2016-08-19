# -*- coding: utf-8 -*-
import decimal
from datetime import datetime
from django.shortcuts import render, redirect
from income.models import Wallets, Transactions, Income, Outcome


def wallets(request):
    wallets, created = Wallets.objects.get_or_create(user = request.user)
    return render(request,'income/wallets.html', {'wallets': wallets})

# TODO:
def transaction(**kwargs):
    wallet_bal = Wallets.objects.get(user=kwargs.get('user'))

    transaction = Transactions.objects.create(
        desc = kwargs.get('desc'),
        amount = kwargs.get('amount'),
        currency = kwargs.get('currency'),
        value_date = kwargs.get('value_date'),
        drcr_ind = kwargs.get('drcr_ind'),
        wallet = wallet_bal,
        user =  kwargs.get('user'),
    )
    transaction.save()
    
    wallet_bal.update_wallet_balance(
        decimal.Decimal(kwargs.get('amount'))
    )


def create_trn(request):
    # form = SomeForm(request.POST or None)
    # if form.is_valid():
    #     obj = form.save()
    #     return redirect('/')
    transaction(
        desc='Desc', 
        amount='100', 
        currency='USD', 
        value_date=datetime.now(), 
        drcr_ind='C', 
        # wallet=, 
        user=request.user
    )
    return redirect('/')
# class SomeForm(forms.ModelForm):
#     class Meta:
#         model = Transactions
#         fields = ('desc', )
