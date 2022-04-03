#!/usr/bin/env python3
import os
import sys
import json


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()

    return json.loads(data)


def get_coins(data):
    coins = []
    for d in data:
        coins.append(d)

    return coins



def get_slopes(data, coins):
    slopes = {}
    for coin in data:
        slopes[coin] = []
        for i in range(0, len(data[coin])-1):
            slope = float(data[coin][i+1]) - float(data[coin][i])
            slopes[coin].append(slope)

    return slopes


def get_avg(slopes):
    averages = {}
    average = 0
    for coin in slopes:
        s = 0
        for slope in slopes[coin]:
            s = s + float(slope)

        if coin == sys.argv[-1]:
            print(f"\n{coin} : {s}")
            print(len(slopes[coin]))
        average = s/float(len(slopes[coin]))
        averages[coin] = average

    return averages


def get_data(data, slopes, averages, coin):
    try:
        print("\nPrices : "+str(data[coin]))
        print("\nSlopes : "+str(slopes[coin]))
        print("\nAverage : "+str(averages[coin]))
        print()
    except:
        pass


def main():
    file_path = 'r2'
    data = read_file(file_path)
    slopes = {}
    averages = {}
    #get number of results
    dataList = list(data)
    numberOfResults = len(data[dataList[0]])

    #get names of coins for dictionary names
    coins = get_coins(data)

    #slope between each value and store them in a dicionary same as data but containing slopes instead of prices
    slopes = get_slopes(data, coins)

    #average of all slopes
    averages = get_avg(data)

    coin = sys.argv[-1]
    get_data(data, slopes, averages, coin)


main()
