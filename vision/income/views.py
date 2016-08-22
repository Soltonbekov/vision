# -*- coding: utf-8 -*-
import decimal
from datetime import datetime
from django.shortcuts import render, redirect
from income.models import Wallets, Transactions, Income, Outcome
from category.models import Category
from income.forms import NewWallet, NewTransaction


def wallets(request):
    wallets, created = Wallets.objects.get_or_create(user = request.user)
    return render(request,'income/wallets.html', {'wallets': wallets})

# TODO:
def transaction(**kwargs):
    wallet = Wallets.objects.get(user=kwargs.get('user'))
    category = Category.objects.get(slug='bill')
    
    transaction = Transactions.objects.create(
        desc = kwargs.get('desc'),
        amount = kwargs.get('amount'),
        currency = kwargs.get('currency'),
        value_date = kwargs.get('value_date'),
        drcr_ind = kwargs.get('drcr_ind'),
        wallet = wallet,
        user =  kwargs.get('user'),
        category = category
    )
    transaction.save()
    
    wallet.update_wallet_balance(
        decimal.Decimal(kwargs.get('amount'))
    )


def create_trn(request):
    # form = SomeForm(request.POST or None)
    # if form.is_valid():
    #     obj = form.save()
    #     return redirect('/')
    transaction(
        desc='For hot water', 
        amount='-5', 
        currency='USD', 
        value_date=datetime.now(), 
        drcr_ind='D', 
        # wallet=, 
        user=request.user
        #category_slug='bill',
    )
    return redirect('/')


def new_wallet(request):
    form = NewWallet(request.POST or None)
    if form.is_valid():
        category = form.save(commit=False)
        category.user = request.user
        category.save()
        return redirect ('/')
    return render(request, 'income/new_wallet.html', {'form': form})


def new_transaction(request):
    form = NewTransaction(request.POST or None)
    if form.is_valid():
        category = form.save(commit=False)
        category.user = request.user
        category.save()
        return redirect ('/')
    return render(request, 'income/new_transaction.html', {'form': form})