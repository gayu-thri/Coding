# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:56:31 2020

@author: egayu
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. INTEGER badIndex
#

def maxIndex(steps, badIndex):
    # Write your code here
    j = 1
    pointer = 0
    while(steps >= 1):

        if pointer + j == badIndex:
            steps -= 1
            continue
        
        pointer = pointer + j 
        j += 1
        steps -= 1

    return pointer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    badIndex = int(input().strip())

    result = maxIndex(steps, badIndex)

    fptr.write(str(result) + '\n')

    fptr.close()
