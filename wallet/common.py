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
