#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = n - 1
    while i >= 0:
        for _ in range(i):
            print(" ",end='')
        for _ in range(n - i):
            print("#",end='')
        print("\n",end='')
        i -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
