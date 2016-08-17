# -*- coding: utf-8 -*-

from django.shortcuts import render
from income.models import Wallets, Transactions, Income, Outcome

# TODO: def return_balance(request):


def wallets(request):
    wallets, created = Wallets.objects.get_or_create(user = request.user)
    return render(request,'income/wallets.html', {'wallets': wallets})


def transaction(**kwargs):
    transaction = Transactions.objects.create(
                desc = kwargs.get('desc'),
                amount = kwargs.get('amount'),
                currency = kwargs.get('currency'),
                value_date = kwargs.get('value_date'),
                drcr_ind = kwargs.get('drcr_ind'),
                wallet = kwargs.get('wallet'),
                user =  kwargs.get('user'),
            )
    transaction.save()

    wallet_bal = Wallets.update_wallet_balance(
                kwargs.get('amount')
            )
    wallet_bal.save()