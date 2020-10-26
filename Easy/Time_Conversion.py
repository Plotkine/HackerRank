#!/bin/python3

import os
import sys

def timeConversion(s):
    if s[-2] == 'P': #PM
        if s[0:2] != '12':
            return str(int(s[0:2]) + 12)+s[2:-2]
        else:
            return s[0:-2]
    else: #AM
            if s[0:2] == '12':
                return '00'+s[2:-2]
            else:
                return s[0:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
