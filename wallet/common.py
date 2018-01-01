""" Common things shared across different files """

COINS = [
    'bitcoin',
]
COIN_TO_NAME = {
    'bitcoin': 'Bitcoin',
}
COIN_TO_UNIT = {
    'bitcoin': 'BTC',
}
def coin_to_display(coin):
    return '{} ({})'.format(COIN_TO_NAME[coin], COIN_TO_UNIT[coin])

ACCOUNTS = [
    'exchange',
    'margin',
    'funding',
]
ACCOUNT_TO_NAME = {
    'exchange': 'Exchange Wallet',
    'margin': 'Margin Wallet',
    'funding': 'Funding Wallet',
}
def get_user_account(username, account):
    return '{}_{}'.format(username, account)
def account_to_display(account):
    return '{}'.format(ACCOUNT_TO_NAME[account])
