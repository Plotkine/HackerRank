#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    (resPos,resNeg,resNull) = (0,0,0)

    for elem in arr:
        if elem > 0:
            resPos += 1/length
        elif elem < 0:
            resNeg += 1/length
        else:
            resNull += 1/length

    print(round(resPos,6))
    print(round(resNeg,6))
    print(round(resNull,6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
