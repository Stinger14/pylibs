import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    v_count = 0
    s_lvl = 0
    for p in path:
        if p == 'U': 
            s_lvl += 1
        if p == 'D':
            s_lvl -= 1
        
        # just came up to sea level increase count
        if (s_lvl == 0 and p == 'U'):
            v_count += 1
    print(v_count)
    return v_count

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()