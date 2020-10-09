from rest_framework import viewsets
from .models import (
    Currency,
    AccountBalance,
    Transaction,
    Wallet
)
from .serializers import (
    WalletSerializer,
    AccountBalanceSerializer,
    CurrencySerializer,
    TransactionSerializer,
    UserSerializer
)

from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WalletViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class AccountBalanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AccountBalance.objects.all()
    serializer_class = AccountBalanceSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
