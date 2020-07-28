# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:57:23 2020

@author: egayu
"""


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isPangram' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY pangram as parameter.
#

def isPangram(pangram):
    # Write your code here
    a = list('abcdefghijklmnopqrstuvwxyz')
    result = ['1' for i in range(len(pangram))]

    index = 0
    for word in pangram:
        for i in a:
            if i not in word:
                result[index] = '0'
                break
        index += 1
            
    return ''.join(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pangram_count = int(input().strip())

    pangram = []

    for _ in range(pangram_count):
        pangram_item = input()
        pangram.append(pangram_item)

    result = isPangram(pangram)

    fptr.write(result + '\n')

    fptr.close()