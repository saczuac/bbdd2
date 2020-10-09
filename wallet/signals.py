from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import (
    Wallet,
    AccountBalance,
    Currency
)


@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if created:
        w = Wallet.objects.create(owner=instance)

        for c in Currency.objects.all():
            AccountBalance.objects.create(currency=c, wallet=w, amount=10000)


@receiver(post_save, sender=Currency)
def currency_created_handler(sender, instance, created, **kwargs):
    if created:
        for u in User.objects.all():
            try:
                AccountBalance.objects.create(
                    currency=instance,
                    wallet=u.wallet,
                    amount=10000
                )
            except:
                # User without wallet
                pass
