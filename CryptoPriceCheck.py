import time
import requests
from datetime import datetime


def crypto_tracker():
    bat_api_url = 'https://min-api.cryptocompare.com/data/price?fsym=BAT&tsyms=USD,JPY,EUR'
    btc_api_url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
    eth_api_url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,JPY,EUR'
    xmr_api_url = 'https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,JPY,EUR'

    btc_info = requests.get(btc_api_url).json()
    bat_info = requests.get(bat_api_url).json()
    eth_info = requests.get(eth_api_url).json()
    xmr_info = requests.get(xmr_api_url).json()

    btc_price = btc_info['USD']
    bat_price = bat_info['USD']
    eth_price = eth_info['USD']
    xmr_price = xmr_info['USD']

    print(datetime.now().strftime('%D %H:%M:%S'), f'BTC PRICE:${btc_price}\n')
    print(datetime.now().strftime('%D %H:%M:%S'), f'BAT PRICE:${bat_price}\n')
    print(datetime.now().strftime('%D %H:%M:%S'), f'ETH PRICE:${eth_price}\n')
    print(datetime.now().strftime('%D %H:%M:%S'),
          f'XMR PRICE:${xmr_price}\n')


def main():
    crypto_tracker()
    while True:
        ch = str(
            input(('\nWould you like to exit or refresh the prices?(Exit E or Refresh R):')))
        if ch in ['E', 'e']:
            return False
        elif ch in ['R', 'r']:
            wait = int(
                input('\nIn how many seconds would you like to refresh?(0 for instantly):'))
            time.sleep(wait)
            crypto_tracker()
        else:
            print('\nPlease enter a vaild answer')


main()
