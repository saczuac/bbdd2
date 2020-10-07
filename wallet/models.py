from django.db import models
from django.conf import settings
import uuid


class Wallet(models.Model):
    is_operative = models.BooleanField(default=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE, related_name="wallet")


class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)


class AccountBalance(models.Model):
    address = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    amount = models.DecimalField(max_digits=34, decimal_places=18, default=0)
    wallet = models.ForeignKey(Wallet,
                               on_delete=models.CASCADE, related_name="balances")
    currency = models.ForeignKey(Currency,
                                 on_delete=models.CASCADE)


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=34, decimal_places=18, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    sent_from = models.ForeignKey(
        AccountBalance, on_delete=models.PROTECT, related_name="transactions")
    sent_to = models.ForeignKey(
        AccountBalance, on_delete=models.PROTECT, related_name="transactions")
