from wallet.api import (
    WalletViewSet,
    CurrencyViewSet,
    AccountBalanceViewSet,
    TransactionViewSet,
    UserViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallets')
router.register(r'currencies', CurrencyViewSet, basename='currencies')
router.register(r'users', UserViewSet, basename='users')
router.register(r'accountbalances', AccountBalanceViewSet,
                basename='accountbalances')
router.register(r'transactions', TransactionViewSet, basename='transactions')
urlpatterns = router.urls
