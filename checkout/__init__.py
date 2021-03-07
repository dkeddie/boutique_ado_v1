default_app_config = 'checkout.apps.CheckoutConfig'

"""
Need to tell Django what the default app is - 
Django wouldn't know about custom ready method, so signals wouldn't work.
"""