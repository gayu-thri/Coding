# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:09:57 2020

@author: egayu
"""

def solution(S):
    sum_of_digits_dict = {}
    
    for i in S:
        sum_of_digits = sum([int(x) for x in str(i)])
        if sum_of_digits in sum_of_digits_dict:
            sum_of_digits_dict[sum_of_digits].append(i)
        else:
            sum_of_digits_dict[sum_of_digits] = [i]
    print(sum_of_digits_dict.items())    
    
    '''
    There must be pairs, if only 1 remove
    '''
    for i in list(sum_of_digits_dict):
        if(len(sum_of_digits_dict[i]) <= 1):
            sum_of_digits_dict.pop(i)    

    '''
    every element in the dict has diff sum
    '''
    if(len(sum_of_digits_dict.keys()) == 0):
        return -1
    print(sum_of_digits_dict.items())   
    
    for i in list(sum_of_digits_dict):
        first_largest_number = max(sum_of_digits_dict[i])
        sum_of_digits_dict[i].remove(first_largest_number)
        second_largest_number = max(sum_of_digits_dict[i])
        sum_of_digits_dict[i] = first_largest_number + second_largest_number
    print(sum_of_digits_dict.items()) 
    
    return max(sum_of_digits_dict.values())
    
print(solution([51,71,17,42,77]))
'''

from collections import defaultdict

s = list(map(int, input().split()))
sumofdigits_dict = defaultdict()

# 51, 71, 17, 42
for i in s:
    sod = sum([int(x) for x in str(i)])
    
    if sod in sumofdigits_dict:
        sumofdigits_dict[sod].append(i)
    else:
        sumofdigits_dict[sod] = [i]

print(sumofdigits_dict.items())    

for i in list(sumofdigits_dict):
    if len(sumofdigits_dict[i]) <= 1:
        sumofdigits_dict.pop(i)
        


if len(sumofdigits_dict.keys()) == 0:
    print(-1)
    exit(0)
    
for i in sumofdigits_dict:
    
    first = max(sumofdigits_dict[i])
    sumofdigits_dict[i].remove(first)
    second = max(sumofdigits_dict[i])
    sumofdigits_dict[i].remove(second)
    sumofdigits_dict[i] = first + second
    
print(max(sumofdigits_dict.values()))

# 51 71 17 42 77
'''