import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    gen_s = ''.join([x for x in s * n])
    s = gen_s[:n]
    return Counter(s).most_common(1)[0][1]


if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
