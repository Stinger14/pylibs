#!/bin/python3

import math
import os
import random
import re
import sys


import requests
#
# Complete the 'getRelevantFoodOutlets' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/food_outlets?city=<city>&page=<pageNumber>
#
# The function is expected to return an array of strings.
# The function accepts a city argument (String) and maxCost argument(Integer).
#

url = 'https://jsonmock.hackerrank.com/api/food_outlets'

def food_outlets_request(url, city, x):
    res = requests.get(url + f'?city={city}&page={x}')
    return res.json()

def parse_json(response, maxCost):
    cities = []
    for i in response['data']:
        city = {
            'name': i['name'],
            'cost': i['estimated_cost'],
        }
        if city['cost'] <= maxCost:
            cities.append(city['name'])
    return cities
    
def get_pages(response):
    return response['total']

def getRelevantFoodOutlets(city, maxCost):
    names = []
    data = food_outlets_request(url, city, 1)
    pages = get_pages(data)


    for x in range(1, pages + 1):
        res = food_outlets_request(url, city, x)
        names.extend(parse_json(res, maxCost))
    return names

print(getRelevantFoodOutlets("Denver", 50))