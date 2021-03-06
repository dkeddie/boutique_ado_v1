from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    """ need to over-ride the ready method, and import the signals receiver"""
    def ready(self):
        import checkout.signals
