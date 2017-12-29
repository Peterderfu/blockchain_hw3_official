from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from .common import COINS, coin_to_display
from .forms import TransferForm


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
        'exchange': exchange,
        'margin': margin,
        'funding': funding,
        'total': exchange + margin + funding,
    }

def _transfer_bitcoin(username, balance, from_wallet, to_wallet, amount):
    conn = _get_conn_bitcoin()

    if balance[from_wallet] >= amount:
        conn.move('{}_{}'.format(username, from_wallet),
                  '{}_{}'.format(username, to_wallet),
                  amount)
        return True
    else:
        return False


""" Views """
@login_required
def index(request):
    username = request.user.username

    global_vars = globals()

    # Balances
    balances = []
    for coin in COINS:
        balance = global_vars['_get_balance_{}'.format(coin)](username)
        balance['coin'] = coin_to_display(coin)
        balances.append(balance)

    # Handle transfer
    if request.method == 'POST':
        transfer_form = TransferForm(request.POST)
        if transfer_form.is_valid():
            coin = transfer_form.cleaned_data['coin']
            from_wallet = transfer_form.cleaned_data['from_wallet']
            to_wallet = transfer_form.cleaned_data['to_wallet']
            amount = transfer_form.cleaned_data['amount']
            if from_wallet == to_wallet:
                msg = 'From- and to-wallets can\'t be the same.'
                transfer_form.add_error('from_wallet', msg)
                transfer_form.add_error('to_wallet', msg)
            elif not global_vars['_transfer_{}'.format(coin)](
                    username,
                    balances[COINS.index(coin)],
                    from_wallet,
                    to_wallet,
                    amount):
                transfer_form.add_error(None, 'You don\'t have enough balance.')
            else:
                return redirect('wallet:index')
    else:
        transfer_form = TransferForm()

    return render(request,
                  'wallet/index.html',
                  {'balances': balances,
                   'transfer_form': transfer_form})
