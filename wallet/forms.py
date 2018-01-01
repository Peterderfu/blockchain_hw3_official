from django import forms

from .common import COINS, coin_to_display, ACCOUNTS, account_to_display


class TransferForm(forms.Form):
    # Helpers
    def _get_coin_choices():
        return [(coin, coin_to_display(coin)) for coin in COINS]
    def _get_wallet_choices():
        return [(account, account_to_display(account)) for account in ACCOUNTS]

    # Fields
    coin = forms.ChoiceField(
        choices=_get_coin_choices()
    )
    from_wallet = forms.ChoiceField(
        choices=_get_wallet_choices()
    )
    to_wallet = forms.ChoiceField(
        choices=_get_wallet_choices()
    )
    amount = forms.DecimalField(
        min_value=0,
        decimal_places=8,
        widget=forms.TextInput(attrs={'placeholder': 'Amount'})
    )

