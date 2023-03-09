from django.contrib import admin

from .models import Account, Owner, Transaction, Vehicle

admin.site.register(Account)
admin.site.register(Owner)
admin.site.register(Transaction)
admin.site.register(Vehicle)
