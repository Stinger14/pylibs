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

def getRelevantFoodOutlets(city, maxCost):
    names = []
    res = requests.get(f'https://jsonmock.hackerrank.com/api/food_outlets?city=Denver&page=1')
    for x in range(0, res.json()['total'] + 1):    
        if res.json()['data'][x]['estimated_cost'] < maxCost:
            names.append(res.json()['data'][x]['name'])
    return names

print(getRelevantFoodOutlets("Denver", 50))