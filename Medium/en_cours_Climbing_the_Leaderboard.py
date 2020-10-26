#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def binary_search_to_insert(arr, low, high, x): 
    # Check base case 
    if high > low: 
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search_to_insert(arr, mid, high, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search_to_insert(arr, low, mid, x) 
    elif high == low:
        # Element is not present in the array 
        return high
    else:
        return "error"

def climbingLeaderboard(ranked, player):
    res = []
    
    for score in player:
        #inserting the score in ranked
        '''i = 0
        while (i < len(ranked)) and ranked[i] > score:
            i += 1'''
        lol = binary_search_to_insert(ranked, 0, len(ranked) - 1, score)
        if lol != "error":
            ranked.insert(lol, score)

        #computing the score's rank and appending it to res
        rank = 1
        previousScore = -1
        i = 0
        while i < len(ranked) and ranked[i] >= score:
            if ranked[i] > score and ranked[i] != previousScore:
                rank += 1
                previousScore = ranked[i]
            i += 1

        res.append(rank)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
