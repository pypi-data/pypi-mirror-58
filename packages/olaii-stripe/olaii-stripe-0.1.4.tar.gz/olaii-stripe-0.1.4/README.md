# Django Olaii Stripe

Stripe wrapper we use at Olaii.com for payment processing. 


## Quick Start

1. Add olaii_stripe to your INSTALLED_APPS settings

```python
INSTALLED_APPS = [
        ...
        'olaii_stripe',
    ]

```

2. Run `python manage.py migrate` to create Stripe models.

3. Add your Stripe API Key to `settings.py`

```python
STRIPE_API_KEY = 'my-api-key'
```