# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.apps import apps
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from wallet.models import Wallet

app = apps.get_app_config('wallet')

for model_name, model in app.models.items():
    admin.site.register(model)


class WalletInline(admin.StackedInline):
    model = Wallet
    can_delete = False
    verbose_name_plural = 'wallets'


class UserAdmin(BaseUserAdmin):
    inlines = (WalletInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
