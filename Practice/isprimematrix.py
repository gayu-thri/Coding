# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:37:58 2020

@author: egayu
"""


def isprime(num):
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                return False    
                break  
            else:  
                return True
    return False
    
def swap(d, b, c):
    l = list(d)
    l[b], l[c] = l[c], l[b]
    return tuple(l)

def NumberOfswapfroTory(matrix):
    values = [(1, 2, 3, 4, 5, 6, 7, 8, 9)]
    possible_exchanges = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 5), (3, 4), (3, 6), (4, 5), (4, 7), (5, 8), (6, 7), (7, 8)]
    bfs = {values[0]: 0}
    
    for i in values:
        temp = []
        for t in possible_exchanges:
            if isprime(i[t[0]] + i[t[1]]):
                temp.append(t)
        for s in temp:
            b = swap(i, s[0], s[1])
            if b not in bfs:
              values.append(b)
              bfs[b] = bfs[i] + 1

    if tuple(matrix) in bfs:
        return bfs[tuple(matrix)]
    return -1
    
print(NumberOfswapfroTory(input()))
