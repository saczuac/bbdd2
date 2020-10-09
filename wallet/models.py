from django.db import models
from django.conf import settings
from django.db import transaction

from .exceptions import (
    WalletIsNotOperative,
    AccountBalanceAmountError,
    CurrencyDoesNotMatchError
)

import uuid


class Wallet(models.Model):
    is_operative = models.BooleanField(default=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE, related_name="wallet")

    class Meta:
        unique_together = ("owner", "id")


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

    def receive(self, amount_to_receive):
        if not (self.wallet.is_operative):
            raise WalletIsNotOperative('Receiver wallet is not operative')

        self.amount = self.amount + amount_to_receive
        self.save()

    def send(self, amount_to_send):
        if not (self.wallet.is_operative):
            raise WalletIsNotOperative('Sender wallet is not operative')

        if (amount_to_send > self.amount):
            raise AccountBalanceAmountError(
                'Sender has not enough balance to send')

        self.amount = self.amount - amount_to_send
        self.save()

    class Meta:
        unique_together = ("wallet", "currency")


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=34, decimal_places=18, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    sent_from = models.ForeignKey(
        AccountBalance, on_delete=models.PROTECT, related_name="transactions_sent")
    sent_to = models.ForeignKey(
        AccountBalance, on_delete=models.PROTECT, related_name="transactions_received")

    @classmethod
    def create(cls, amount, sent_from, sent_to):
        if (sent_from.currency != sent_to.currency):
            raise CurrencyDoesNotMatchError(
                'Sender currency and receiver currency are not the same')

        txn = cls(
            sent_to=sent_to,
            sent_from=sent_from,
            amount=amount
        )

        with transaction.atomic():
            sent_from.send(amount)
            sent_to.receive(amount)
            txn.save()

        return txn

import wallet.signals
