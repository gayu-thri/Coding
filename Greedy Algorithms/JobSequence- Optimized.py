# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:40:58 2020

@author: egayu
"""
def cmp(a):
    return a['profit']

def schedulejob(arr,n):
    
    #Sorts the profits in descending order
    arr = sorted(arr, key = cmp, reverse = True)
    
            
if __name__ == '__main__':
    arr = [{'id': 'a', 'deadline': 2, 'profit': 120}, 
           {'id': 'b', 'deadline': 1, 'profit': 20}, 
           {'id': 'c', 'deadline': 2, 'profit': 35}, 
           {'id': 'd', 'deadline': 1, 'profit': 22}, 
           {'id': 'e', 'deadline': 3, 'profit': 11}] 
    
    print('Maximum profit sequence of jobs: ')
    print(schedulejob(arr, len(arr)))
