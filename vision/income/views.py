# -*- coding: utf-8 -*-

from django.shortcuts import render
from income.models import Wallets, Transactions, Income, Outcome

# TODO: def return_balance(request):


def wallets(request):
    wallets, created = Wallets.objects.get_or_create(user = request.user)
    return render(request,'income/wallets.html', {'wallets': wallets})
