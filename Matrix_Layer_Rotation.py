#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy

# Complete the matrixRotation function below.
def matrixRotation(matrix,r):
    res = deepcopy(matrix)
    m = len(matrix)
    n = len(matrix[0])

    for _ in range(r):
        ring = 0
        while ring <= min(m,n) / 2:
            resCopy = deepcopy(res)
            i = ring
            j = ring
            #going right
            while j + 1 < n - ring:
                res[i][j] = resCopy[i][j+1]
                j += 1
            #going down
            while i + 1 < m - ring:
                res[i][j] = resCopy[i+1][j]
                i += 1
            #going left
            while j - 1 >= ring:
                res[i][j] = resCopy[i][j-1]
                j -= 1
            #going up
            while i - 1 >= ring:
                res[i][j] = resCopy[i-1][j]
                i -= 1
            ring += 1

    #print("")
    for i in range(len(res)):
        for j in range(len(res[0]) - 1):
                print(str(res[i][j])+" ",end='')
        print(str(res[i][len(res[0]) - 1]),end='')
        if i != len(res) - 1:
            print("\n",end='')


if __name__ == '__main__':
    mnr = input().rstrip().split()
    m = int(mnr[0])
    n = int(mnr[1])
    r = int(mnr[2])

    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
