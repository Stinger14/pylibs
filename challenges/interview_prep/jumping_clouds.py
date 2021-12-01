import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    move, jump = 0, 0
    while move < len(c) - 2:
        move = move + 1 if c[move + 2] else move + 2
        jump += 1
    if move < len(c) - 1:
        jump += 1
    return jump


if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()