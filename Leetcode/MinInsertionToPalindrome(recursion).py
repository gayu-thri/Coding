# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:36:45 2020

@author: egayu
"""
def findmin(s):
    print(s)
    if s == s[::-1]:
        return 0
    if s[0] == s[-1]:
        return findmin(s[1:-1])
    else:
        return 1 + min(findmin(s[1:]), findmin(s[:-1]))

    
s = "abcdecba"
n = findmin(s)
print(n)
