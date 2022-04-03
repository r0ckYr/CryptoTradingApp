#!/usr/bin/env python3

import requests
import json
import time

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def send_request(url):
    try:
        r = requests.get(url, timeout=10)
        return r
    except Exception as e:
        print(str(e))
        return None


def print_screen(avg, price):
    diff=avg-price
    gap=0
    if diff<0:
        gap1=diff/100
        gap=50-diff
    elif diff>0:
        gap=diff/100
    else:
        gap=0

    gap=int(gap)*3
    if diff != 0:
        f = 0
        if gap > 51:
            f = 1
        for i in range(1,102):
            if(i==gap):
                if i < 51:
                    print(f'{FAIL}|{ENDC}',end='')
                    f = -1
                elif i > 51:
                    print(f'{OKGREEN}|{ENDC}',end='')
                    f = 0
            elif i == 51:
                print(f'{OKBLUE}|{ENDC}',end='')
                if f == -1:
                    f = 0
            else:
                if f == -1:
                    print(f'{FAIL}|{ENDC}',end='')
                elif f == 1 and i > 51:
                    print(f'{OKGREEN}|{ENDC}',end='')
                else:
                    print(' ', end='')


        print(f' : {HEADER}{str(price)}{ENDC}')


def main():
    # url  = 'https://api.wazirx.com/sapi/v1/exchangeInfo'
    url = 'https://api.wazirx.com/sapi/v1/tickers/24hr'
    prices = []
    c = 0
    s = 0
    avg_number = 2.0
    while True:
        r = send_request(url)
        if r is not None:
            data = json.loads(r.text)
            price = float(data[0]["lastPrice"])
            if c < avg_number:
                prices.append(price)
                s = s+price
                c = c + 1
            else:
                avg = s/avg_number
                print_screen(avg, price)
        time.sleep(1)


main()
