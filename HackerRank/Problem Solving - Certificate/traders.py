#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    # Write your code here
    atleast = float((5 * len(customers))/100)
    print(atleast)
    cust_set = set(customers)
    print(cust_set)
    mydict = {i:0 for i in cust_set}
    print(mydict)
    result = []

    for i in customers:
        mydict[i] += 1
    print(mydict)
    for key,val in mydict.items():
        
        if val >= atleast:
            result.append(key)
    
    result.sort()
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
