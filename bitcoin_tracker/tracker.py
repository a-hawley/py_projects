import requests
from os import name, system

url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
exit_flag = False

while not exit_flag:
    api = requests.get(url)
    json = api.json()
    system('cls' if name == 'nt' else 'clear')
    for key in json:
        print(f'{key}: {json[key]}\n')
