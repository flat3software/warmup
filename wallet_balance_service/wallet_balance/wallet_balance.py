import requests
from wallet_balance_service.wallet_balance.erc20_address_lookup import ERC20_INFO

api_key = 'FUUJPFTN972AQ6K7CGIB9R4ARGG28JCEX8'
ether_wallet_api = 'https://api.etherscan.io/api?module=account&action=balance&address={0}&tag=latest&apikey={1}'
token_ether_wallet_api = 'https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={0}&' \
                         'address={1}&tag=latest&apikey={2}'


def get_token_balance(wallet_public_key, token_symbol):
    if token_symbol.lower() == 'eth':
        return get_eth_balance(wallet_public_key)

    token_info = ERC20_INFO[token_symbol]
    response = requests.get(token_ether_wallet_api.format(token_info['address'], wallet_public_key, api_key)).json()
    return int(response['result']) * (10 ** -token_info['decimal'])


def get_eth_balance(wallet_public_key):
    response = requests.get(ether_wallet_api.format(wallet_public_key, api_key)).json()
    return convert_wei_to_eth(response['result'])


def convert_wei_to_eth(wei):
    return int(wei) / 1000000000000000000
