#!/usr/bin/env python3
import sys
import os
import time
import requests
import json

result = {}


def send_request(url):
    r = None
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except Exception as e:
        print(str(e))
        return None



def get_coins(data):
    coins = []
    for d in data:
        symbol = d["symbol"]
        if symbol.endswith('inr') and symbol not in coins:
            coins.append(symbol)

    return coins


def start(url):
    startTime = time.perf_counter()
    while True:
        try:

            currnetTime = time.perf_counter()
            timePassed = currnetTime - startTime
            if timePassed >= 10:
                break
            data = json.loads(send_request(url))
            if data is not None:
                for d in data:
                    symbol = d["symbol"]
                    if symbol.endswith('inr'):
                        price = d["lastPrice"]
                        result[symbol].append(price)
        except Exception as e:
            print('error')

        time.sleep(1)

    #write 2hr data to file
    with open('result.out', 'w') as f:
        f.write(str(result))

    print(result)


def main():
    #url to download coins data
    url = 'https://api.wazirx.com/sapi/v1/tickers/24hr'

    #get data form the api
    data = json.loads(send_request(url))

    #store name of coins in a array
    coins = get_coins(data)

    #store coins in a dictionary with value = a empty list
    for coin in coins:
        result[coin] = []

    time.sleep(1)

    start(url)



main()
