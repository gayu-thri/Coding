# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:59:55 2020

@author: egayu
"""

def printJobScheduling(arr, t): 
  
    # length of array 
    n = len(arr) 
  
    # Sort all jobs according to  
    # decreasing order of profit 
    for i in range(n): 
        for j in range(n - 1 - i): 
            if arr[j][2] < arr[j + 1][2]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
  
    #free time slots 
    slots = [False] * t 
  
    # To store result (Sequence of jobs) 
    result = ['-1'] * t 
  
    for i in range(len(arr)): 
  
        # Find a free slot for this job  
        # (Note that we start from the  
        # last possible slot) 
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1): 
              
            # Free slot found 
            if slots[j] is False: 
                slots[j] = True
                result[j] = arr[i][0] 
                break
            
    print(result) 
  
if __name__ == '__main__':
    arr = [['a', 2, 100], # Job Array 
           ['b', 1, 19], 
           ['c', 2, 27], 
           ['d', 1, 25], 
           ['e', 3, 15]] 
      
      
    print("Maximum profit sequence of jobs: ") 
    printJobScheduling(arr, 3) # Function Call 
      