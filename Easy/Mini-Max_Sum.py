#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy

def find4Min(arr): #returns array with 4 smallest elements of arr
    temp = [10**9,10**9,10**9,10**9]
    for elem in arr:
        if elem < temp[3]:
            temp[0] = temp[1]
            temp[1] = temp[2]
            temp[2] = temp[3]
            temp[3] = elem
        elif elem < temp[2]:
            temp[0] = temp[1]
            temp[1] = temp[2]
            temp [2] = elem
        elif elem < temp[1]:
            temp[0] = temp[1]
            temp[1] = elem
        elif elem < temp[0]:
            temp [0] = elem
    return temp[0]+temp[1]+temp[2]+temp[3]

# Complete the miniMaxSum function below.
def find4Max(arr): #returns array with 4 largest elements of arr
    temp = [1,1,1,1]
    for elem in arr:
        if elem > temp[3]:
            temp[0] = temp[1]
            temp[1] = temp[2]
            temp[2] = temp[3]
            temp[3] = elem
        elif elem > temp[2]:
            temp[0] = temp[1]
            temp[1] = temp[2]
            temp [2] = elem
        elif elem > temp[1]:
            temp[0] = temp[1]
            temp[1] = elem
        elif elem > temp[0]:
            temp [0] = elem
    return temp[0]+temp[1]+temp[2]+temp[3]

def miniMaxSum(arr):
    temp = deepcopy(arr)
    print(str(find4Min(arr))+" ", end='')
    print(str(find4Max(arr)), end='')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
