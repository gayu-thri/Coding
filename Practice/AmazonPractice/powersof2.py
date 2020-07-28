# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:57:20 2020

@author: egayu
"""


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isPower' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def isPower(arr):
    # Write your code here
    result = []

    i = 0

    for n in arr:
        if(n>0):
            result.append('1' if n & n-1 == 0 else '0')
        else:
            result.append('0')

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = isPower(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()