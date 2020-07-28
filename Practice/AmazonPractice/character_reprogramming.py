# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 20:01:58 2020

@author: egayu
"""


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxDeletions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getMaxDeletions(s):
    # Write your code here
    #initial = [0,0]
    destination = [0,0]
    for i in s:
        if i == 'U':
            destination[1] += 1
        elif i == 'D':
            destination[1] -= 1
        elif i == 'L':
            destination[0] -= 1
        elif i == 'R':
            destination[0] += 1

    #print(destination)

    minumum_moves = max(destination[0] + 0,destination[1] + 0)
    deletions = len(s) - minumum_moves
    return deletions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getMaxDeletions(s)

    fptr.write(str(result) + '\n')

    fptr.close()
