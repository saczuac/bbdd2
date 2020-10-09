from rest_framework import serializers
from .models import Currency, AccountBalance, Transaction, Wallet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Wallet
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        txn = Transaction.create(
            validated_data.get("amount"),
            validated_data.get("sent_from"),
            validated_data.get("sent_to")
        )

        return txn


class AccountBalanceSerializer(serializers.ModelSerializer):
    currency = serializers.ReadOnlyField(source='currency.symbol')
    owner = serializers.SerializerMethodField()

    def get_owner(self, obj):
        return obj.wallet.owner.username

    class Meta:
        model = AccountBalance
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
