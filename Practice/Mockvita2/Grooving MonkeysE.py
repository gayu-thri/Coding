# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:31:21 2020

@author: egayu
"""
def findtime(monkeys):
    time = 0
    original = []
    original.insert(0,'X')
    
    for i in range(1,len(monkeys)+1):
        original.insert(i,i)
    
    if original[1:] == monkeys:
        return 0
    
    swap = original
    
    for i in range(1,len(monkeys)+1):
        
        temp = swap[monkeys[i-1]]
        swap[monkeys[i-1]] = swap[i]
        swap[monkeys[temp-1]] = temp
        
        print(swap)
        
        time += 1
        
        if swap == original:
            break
    
    return time

t = int(input())
for i in range(t):
    n = int(input())
    monkeys = list(map(int,input().split()))
    print(findtime(monkeys))