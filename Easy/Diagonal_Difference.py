#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    length = len(arr)

    diagSum1 = 0
    for i in range(length):
        diagSum1 += arr[i][i]
    
    diagSum2 = 0
    j = length - 1
    for i in range(length):
        diagSum2 += arr[i][j]
        j -= 1
    return abs(diagSum1 - diagSum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
