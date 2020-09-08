# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:41:23 2020

@author: egayu
"""

def findfreq(string):
    n = len(string)
        #count = 0 
        
    string = sorted(string) ##sorted initiallyyy
    d = dict()
    for i in range(n):
            
            if(string[i] in d.keys()) :
                d[string[i]] += 1
            else:
                d[string[i]] = 1
                
    #return ''.join("{!s}{!r}".format(key,val) for (key,val) in d.items())
    return ''.join("{!r}{!s}".format(val,key) for (key,val) in d.items())

if __name__ == '__main__': 
      
    # Calling function 
    out = findfreq(input()) 
    print("Element with its frequency")
    print(out)
    
    '''
    for i in range(n):
            
            if(string[i] not in d):
                count = 1
            for j in range(i+1,n):
                if(string[i]==string[j]):
                    count = count+1
            d[string[i]] = count
    '''