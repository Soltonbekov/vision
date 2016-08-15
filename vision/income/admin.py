from django.contrib import admin

from income.models import Wallets, Transactions, Income, Outcome

admin.site.register(Wallets)
admin.site.register(Transactions)
admin.site.register(Income)
admin.site.register(Outcome)
