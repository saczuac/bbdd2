from django.apps import AppConfig


class WalletConfig(AppConfig):
    name = 'wallet'

    def ready(self):
        super(WalletConfig, self).ready()
