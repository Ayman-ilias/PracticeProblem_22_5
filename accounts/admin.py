# admin.py

from django.contrib import admin
from .models import UserBankAccount, UserAddress

class UserBankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_no', 'balance', 'is_bankrupt')
    actions = ['is_bankrupt', 'make_solvent']

    def make_bankrupt(self, request, queryset):
        queryset.update(bankrupt=True)

    def make_solvent(self, request, queryset):
        queryset.update(bankrupt=False)

# Register the models and admin classes
admin.site.register(UserBankAccount, UserBankAccountAdmin)
admin.site.register(UserAddress)
