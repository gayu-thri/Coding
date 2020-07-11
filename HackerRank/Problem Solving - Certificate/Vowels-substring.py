#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    # Write your code here
    max_count = 0
    string = ''
    vowels = {'a','e','i','o','u'}
    n = len(s)
    flag = 0
    for i in range(0,k):
        if s[i] in vowels:
            flag = 1
            max_count += 1

    string = s[0:k]
    cur = max_count
    for i in range(1,n-k+1):

        if s[i-1] in vowels:
            cur = cur - 1
        if s[i+k-1] in vowels:
            cur = cur + 1

        if cur > max_count:
            flag = 1
            string = s[i:i+k]
            max_count = cur

    if flag == 0:
        return "Not found!"
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()
