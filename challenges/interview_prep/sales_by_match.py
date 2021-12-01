#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # c = {x: ar.count(x) for x in ar}
    c = dict(Counter(ar))
    pairs = 0

    for x in c.values():
        if x > 1:
            while x:
                pairs += 1
                x -= 2
                if x == 1:
                    break

    return pairs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # ar = list(map(int, input().rstrip().split()))
    #
    # result = sockMerchant(n, ar)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    res = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    print(res)
