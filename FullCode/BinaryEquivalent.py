# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 07:34:30 2020

@author: egayu
"""
import sys

while True:
    try:
        N = int(input())
        if N < 1 or N > 20:
            raise ValueError 
        break
    except ValueError:
        sys.exit()
        
arr = list(map(int,input().split(' ')))

binary = []
for i in range(len(arr)):
    binary.insert(i, bin(arr[i]).replace('0b',''))

max_len = len(max(binary, key = len))


#mydict = {}
mylist = []
for i in range(len(arr)):
    if max_len != len(binary[i]):
        #mydict[arr[i]] = [(('0' * (max_len - len(binary[i]))) + binary[i]).count('1'),(('0' * (max_len - len(binary[i]))) + binary[i]).count('0')]
        mylist.append([(('0' * (max_len - len(binary[i]))) + binary[i]).count('1'),(('0' * (max_len - len(binary[i]))) + binary[i]).count('0')])
    else:
        #mydict[arr[i]] = [binary[i].count('1'), binary[i].count('0')]
        mylist.append([binary[i].count('1'), binary[i].count('0')])

count_odd = 0
count_even = 0

    # Find sum of all subsequences with even count 
    # and odd count and storing them as we iterate. 

for i in range(N): 
  
    # if the number is even 
    if mylist[i - 1][0] % 2 == 0 and mylist[i - 1][1] % 2 == 0: 
        count_even = count_even + count_even + 1
        count_odd = count_odd + count_odd 
  
    # if the number is odd 
    else: 
        temp = count_even 
        count_even = count_even + count_odd 
        count_odd = count_odd + temp + 1
      
#print( [count_even, count_odd] )
appendzero = max_len - len(bin(count_even).replace('0b',''))
result = ('0' * appendzero) + bin(count_even).replace('0b','')  
print(result)
        
    
# if no binary equivalent
        # print('0'*max_len)
        

#to_append_or = ('0' * max_len)

'''
b = ''
to_append_or = b.zfill(max_len)

for i in range(len(arr)):
    
    arr[i] = arr[i] | 0x0000
'''
