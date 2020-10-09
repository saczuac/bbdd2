from rest_framework import exceptions


class TransactionError(Exception):
    pass


class WalletIsNotOperative(TransactionError):
    pass


class AccountBalanceAmountError(TransactionError):
    pass


class CurrencyDoesNotMatchError(TransactionError):
    pass
