#!/bin/python3
import sys
from itertools import accumulate

# TODO Divide arr in two halves
# TODO Get sum of each half
# TODO If sum of each half is the same return first half's last element index


def balance_array(arr):
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    for i in arr:
        print(i)


if __name__ == "__main__":
    a = list(map(int, input().strip().split(' ')))
    result = balance_array(a)


    print(result)
