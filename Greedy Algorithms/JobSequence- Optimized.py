# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:40:58 2020

@author: egayu
"""
import sys

class disjointset:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
    
    def find(self, s):
        if s == self.parent[s]:
            return s
        self.parent[s] = self.find(self.parent[s])
        return self.parent[s]
    
    def merge(self, u, v):
        self.parent[v] = u
    
def cmp(a):
    return a['profit']

def findmaxdeadline(arr,n):
    ans = -sys.maxsize - 1
    for i in range(n):
        ans = max(ans, arr[i]['deadline'])
    return ans

def schedulejob(arr,n):
    
    #sort according to profit
    arr = sorted(arr, key = cmp, reverse = True)
    
    maximum = findmaxdeadline(arr,n)
    ds = disjointset(maximum)
    
    for i in range(n):
        available_slot = ds.find(arr[i]['deadline'])
        if available_slot > 0:
            ds.merge(ds.find(available_slot - 1), available_slot)
            print(arr[i]['id'], end = ' ')
            
if __name__ == '__main__':
    arr = [{'id': 'a', 'deadline': 2, 'profit': 120}, 
           {'id': 'b', 'deadline': 1, 'profit': 20}, 
           {'id': 'c', 'deadline': 2, 'profit': 35}, 
           {'id': 'd', 'deadline': 1, 'profit': 22}, 
           {'id': 'e', 'deadline': 3, 'profit': 11}] 
    
    print('Maximum profit sequence of jobs: ')
    print(schedulejob(arr, len(arr)))
