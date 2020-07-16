# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:44:32 2020

@author: egayu
"""
string = list(input('Enter the string: '))

alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alpha = dict()
i = 0

for char in alphabets:
    alpha[char] = i
    i += 1
    
prev = string[0]
sum = min(26 - alpha[prev], alpha[prev])

#print(alpha)
for i in range(1,len(string)): 
    
    sum += min(26 - abs(alpha[string[i]] - alpha[prev]), abs(alpha[string[i]] - alpha[prev]))
    prev = string[i]
    
print("Minimum sum required: ", sum)