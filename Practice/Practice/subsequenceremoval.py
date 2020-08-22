# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:57:21 2020

@author: egayu
"""


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findSubsequence(arr):
    # Write your code here
    result = []
    appended = -sys.maxsize
    freq = {}
    if arr.sort(reverse = True) == arr:
        return ['-1']
    
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
        if freq[i] > 1 and i >= appended:
            result.append(i)
            appended = i
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = findSubsequence(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
