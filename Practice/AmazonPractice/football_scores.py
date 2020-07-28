# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:57:24 2020

@author: egayu
"""


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'counts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY teamA
#  2. INTEGER_ARRAY teamB
#

def counts(teamA, teamB):
    # Write your code here
    def binary_search(teamA,b):
        left = 0
        right = len(teamA) - 1

        while(left <= right):
            mid = left + (right - left)//2
            if teamA[mid] <= b:
                left = mid + 1
            else:
                right= mid - 1

        return right

    teamA.sort()
    result = []
    for i in range(len(teamB)):
        index = binary_search(teamA,teamB[i])
        result.append(index+1)
    return result

    '''
    result = []
    n = 0
    for b in teamB:
        i = 0
        n = 0
        while(i<len(teamA)):
            if teamA[i] <= b:
                n += 1
            i += 1
        result.append(n)
    return result
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    teamA_count = int(input().strip())

    teamA = []

    for _ in range(teamA_count):
        teamA_item = int(input().strip())
        teamA.append(teamA_item)

    teamB_count = int(input().strip())

    teamB = []

    for _ in range(teamB_count):
        teamB_item = int(input().strip())
        teamB.append(teamB_item)

    result = counts(teamA, teamB)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
