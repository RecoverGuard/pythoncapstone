# This script will generate a table of the top 10 Cryptocurrencies with real-time data metrics from the CMC API
# !/usr/bin/env python3
"""Author: James Vinciguerra"""

# BEGIN COINMARKETCAP API
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from prettytable import PrettyTable
from colorama import Fore, Style
from datetime import datetime

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '10',  # SETS UPPER LIMIT OF WHICH RANKINGS TO EXTRACT
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '131a4d4b-7b05-49de-8d5a-19d15b4e86d1',  # UNIQUE KEY
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


# END OF COINMARKETCAP API SCRIPT

# THIS FUNCTION ASSIGNS THE VARIABLES NEEDED TO EXTRACT THE PROPER DATA FROM THE API FOR THE TOP 10
# CRYPTOCURRENCIES BY MARKET CAP
def extract_data():
    # DISPLAY CURRENT RANK BY MARKET CAP
    rank = data['data'][0]['cmc_rank']
    rank_2 = data['data'][1]['cmc_rank']
    rank_3 = data['data'][2]['cmc_rank']
    rank_4 = data['data'][3]['cmc_rank']
    rank_5 = data['data'][4]['cmc_rank']
    rank_6 = data['data'][5]['cmc_rank']
    rank_7 = data['data'][6]['cmc_rank']
    rank_8 = data['data'][7]['cmc_rank']
    rank_9 = data['data'][8]['cmc_rank']
    rank_10 = data['data'][9]['cmc_rank']

    # TICKERS
    name = data['data'][0]['name']
    name_2 = data['data'][1]['name']
    name_3 = data['data'][2]['name']
    name_4 = data['data'][3]['name']
    name_5 = data['data'][4]['name']
    name_6 = data['data'][5]['name']
    name_7 = data['data'][6]['name']
    name_8 = data['data'][7]['name']
    name_9 = data['data'][8]['name']
    name_10 = data['data'][9]['name']

    # CURRENT MARKET CAP
    mcap = int(data['data'][0]['quote']['USD']['market_cap'])
    mcap_2 = int(data['data'][1]['quote']['USD']['market_cap'])
    mcap_3 = int(data['data'][2]['quote']['USD']['market_cap'])
    mcap_4 = int(data['data'][3]['quote']['USD']['market_cap'])
    mcap_5 = int(data['data'][4]['quote']['USD']['market_cap'])
    mcap_6 = int(data['data'][5]['quote']['USD']['market_cap'])
    mcap_7 = int(data['data'][6]['quote']['USD']['market_cap'])
    mcap_8 = int(data['data'][7]['quote']['USD']['market_cap'])
    mcap_9 = int(data['data'][8]['quote']['USD']['market_cap'])
    mcap_10 = int(data['data'][9]['quote']['USD']['market_cap'])

    # LIST CURRENT PRICE
    price = round(data['data'][0]['quote']['USD']['price'], 2)
    price_2 = round(data['data'][1]['quote']['USD']['price'], 2)
    price_3 = round(data['data'][2]['quote']['USD']['price'], 2)
    price_4 = round(data['data'][3]['quote']['USD']['price'], 2)
    price_5 = round(data['data'][4]['quote']['USD']['price'], 2)
    price_6 = round(data['data'][5]['quote']['USD']['price'], 2)
    price_7 = round(data['data'][6]['quote']['USD']['price'], 2)
    price_8 = round(data['data'][7]['quote']['USD']['price'], 2)
    price_9 = round(data['data'][8]['quote']['USD']['price'], 2)
    price_10 = round(data['data'][9]['quote']['USD']['price'], 2)

    # 24 HOUR TRADING VOLUME
    volume = int(data['data'][0]['quote']['USD']['volume_24h'])
    volume_2 = int(data['data'][1]['quote']['USD']['volume_24h'])
    volume_3 = int(data['data'][2]['quote']['USD']['volume_24h'])
    volume_4 = int(data['data'][3]['quote']['USD']['volume_24h'])
    volume_5 = int(data['data'][4]['quote']['USD']['volume_24h'])
    volume_6 = int(data['data'][5]['quote']['USD']['volume_24h'])
    volume_7 = int(data['data'][6]['quote']['USD']['volume_24h'])
    volume_8 = int(data['data'][7]['quote']['USD']['volume_24h'])
    volume_9 = int(data['data'][8]['quote']['USD']['volume_24h'])
    volume_10 = int(data['data'][9]['quote']['USD']['volume_24h'])

    # 24 HOUR PRICE CHANGE
    movement = round(data['data'][0]['quote']['USD']['percent_change_24h'], 2)
    movement_2 = round(data['data'][1]['quote']['USD']['percent_change_24h'], 2)
    movement_3 = round(data['data'][2]['quote']['USD']['percent_change_24h'], 2)
    movement_4 = round(data['data'][3]['quote']['USD']['percent_change_24h'], 2)
    movement_5 = round(data['data'][4]['quote']['USD']['percent_change_24h'], 2)
    movement_6 = round(data['data'][5]['quote']['USD']['percent_change_24h'], 2)
    movement_7 = round(data['data'][6]['quote']['USD']['percent_change_24h'], 2)
    movement_8 = round(data['data'][7]['quote']['USD']['percent_change_24h'], 2)
    movement_9 = round(data['data'][8]['quote']['USD']['percent_change_24h'], 2)
    movement_10 = round(data['data'][9]['quote']['USD']['percent_change_24h'], 2)

    # SETTING COLOR CHANGES TO REPRESENT PRICE MOVEMENTS
    if movement > 0:
        movement = Fore.GREEN + str(movement) + '%' + Style.RESET_ALL
    else:
        movement = Fore.RED + str(movement) + '%' + Style.RESET_ALL

    if movement_2 > 0:
        movement_2 = Fore.GREEN + str(movement_2) + '%' + Style.RESET_ALL
    else:
        movement_2 = Fore.RED + str(movement_2) + '%' + Style.RESET_ALL

    if movement_3 > 0:
        movement_3 = Fore.GREEN + str(movement_3) + '%' + Style.RESET_ALL
    else:
        movement_3 = Fore.RED + str(movement_3) + '%' + Style.RESET_ALL

    if movement_4 > 0:
        movement_4 = Fore.GREEN + str(movement_4) + '%' + Style.RESET_ALL
    else:
        movement_4 = Fore.RED + str(movement_4) + '%' + Style.RESET_ALL

    if movement_5 > 0:
        movement_5 = Fore.GREEN + str(movement_5) + '%' + Style.RESET_ALL
    else:
        movement_5 = Fore.RED + str(movement_5) + '%' + Style.RESET_ALL

    if movement_6 > 0:
        movement_6 = Fore.GREEN + str(movement_6) + '%' + Style.RESET_ALL
    else:
        movement_6 = Fore.RED + str(movement_6) + '%' + Style.RESET_ALL

    if movement_7 > 0:
        movement_7 = Fore.GREEN + str(movement_7) + '%' + Style.RESET_ALL
    else:
        movement_7 = Fore.RED + str(movement_7) + '%' + Style.RESET_ALL

    if movement_8 > 0:
        movement_8 = Fore.GREEN + str(movement_8) + '%' + Style.RESET_ALL
    else:
        movement_8 = Fore.RED + str(movement_8) + '%' + Style.RESET_ALL

    if movement_9 > 0:
        movement_9 = Fore.GREEN + str(movement_9) + '%' + Style.RESET_ALL
    else:
        movement_9 = Fore.RED + str(movement_9) + '%' + Style.RESET_ALL

    if movement_10 > 0:
        movement_10 = Fore.GREEN + str(movement_10) + '%' + Style.RESET_ALL
    else:
        movement_10 = Fore.RED + str(movement_10) + '%' + Style.RESET_ALL

    # COMPILING DATA INTO TABLE FORMAT
    def execute_data():

        table = PrettyTable()
        table.field_names = (Fore.LIGHTCYAN_EX + 'RANK', 'CRYPTOCURRENCY', 'MARKET CAP', 'PRICE', '24H VOLUME',
                             '24H CHANGE' + Style.RESET_ALL)
        table.add_row([rank, name, '${:,}'.format(mcap), '${:,}'.format(price), '${:,}'.format(volume), movement])
        table.add_row([rank_2, name_2, '${:,}'.format(mcap_2), '${:,}'.format(price_2), '${:,}'.format(volume_2),
                       movement_2])
        table.add_row([rank_3, name_3, '${:,}'.format(mcap_3), '${:,}'.format(price_3), '${:,}'.format(volume_3),
                       movement_3])
        table.add_row([rank_4, name_4, '${:,}'.format(mcap_4), '${:,}'.format(price_4), '${:,}'.format(volume_4),
                       movement_4])
        table.add_row([rank_5, name_5, '${:,}'.format(mcap_5), '${:,}'.format(price_5), '${:,}'.format(volume_5),
                       movement_5])
        table.add_row([rank_6, name_6, '${:,}'.format(mcap_6), '${:,}'.format(price_6), '${:,}'.format(volume_6),
                       movement_6])
        table.add_row([rank_7, name_7, '${:,}'.format(mcap_7), '${:,}'.format(price_7), '${:,}'.format(volume_7),
                       movement_7])
        table.add_row([rank_8, name_8, '${:,}'.format(mcap_8), '${:,}'.format(price_8), '${:,}'.format(volume_8),
                       movement_8])
        table.add_row([rank_9, name_9, '${:,}'.format(mcap_9), '${:,}'.format(price_9), '${:,}'.format(volume_9),
                       movement_9])
        table.add_row([rank_10, name_10, '${:,}'.format(mcap_10), '${:,}'.format(price_10), '${:,}'.format(volume_10),
                       movement_10])

        print()
        print(Fore.LIGHTMAGENTA_EX + 'CURRENT PRICE METRICS FOR TOP 10 CRYPTOCURRENCIES BY MARKET CAP'
              + Style.RESET_ALL)
        print(table)

        # LAST UPDATED TIME
        last_updated = datetime.today().strftime('%B %d, %Y at %I:%M%p')
        print('This table was last updated on: ' + last_updated)

    # CALL NESTED FUNCTION
    execute_data()


# CALL MAIN FUNCTION
extract_data()
