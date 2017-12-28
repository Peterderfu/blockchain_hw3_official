from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


""" Bitcoin Wallet """
def _get_conn_bitcoin():
    rpcuser = 'ntu2b'
    rpcpassword = 'ntuhw1234'
    # rpcconnect = '52.179.99.176'
    rpcconnect = '127.0.0.1'
    rpcport = 8332
    return AuthServiceProxy('http://{}:{}@{}:{}'.format(rpcuser, rpcpassword, rpcconnect, rpcport))

def _get_balance_bitcoin(username):
    conn = _get_conn_bitcoin()

    exchange = conn.getbalance(username + '_exchange')
    margin = conn.getbalance(username + '_margin')
    funding = conn.getbalance(username + '_funding')

    return {
        'name': 'Bitcoin (BTC)',
        'exchange': exchange,
        'margin': margin,
        'funding': funding,
        'total': exchange + margin + funding
    }


""" Views """
@login_required
def index(request):
    username = request.user.username

    coins = ['bitcoin']
    global_vars = globals()

    # Balances
    balances = []
    for coin in coins:
        balances.append(global_vars['_get_balance_{}'.format(coin)](username))

    return render(request,
                  'wallet/index.html',
                  {'balances': balances})
