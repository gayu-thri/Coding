# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:26:29 2020

@author: egayu
"""
import sys
d = dict()

while(True):
    i = input()
    if int(i) == -1:
        sys.exit(0)
    
    l = i.split(" ")
    
    if l[0] == 'A':
      d[int(l[1])] = int(l[2]) 
      
    elif l[0] == 'Q':
        
        if l[1] == '1':
            if int(l[2]) in d.keys():
                print(True)
            else:
                print(False)
        if l[1] == '2':
            c = 0
            for e_id in d.keys():
                if str(e_id).startswith(l[2]):
                    c += 1
            print(c)
        if l[1] == '3':
            c = 0
            for key,val in d.items():
                if str(key).startswith(l[2]):
                    if val < int(l[4]) and val > int(l[3]):
                        c += 1
            print(c)
    print(d)
'''
Sample Input:

A 112345 20
A 112346 40
A 212347 40
A 212348 23
A 112449 30
Q 1 112345
Q 2 1123
Q 3 112 10 50
-1

Sample Output:

True
2
3

Submissions: 0
Max Score: 100
Difficulty: Easy
Rate This Challenge:

    
More

'''