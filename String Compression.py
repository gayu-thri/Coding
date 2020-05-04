# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:30:57 2020

@author: egayu
"""

class Solution:
    def compress(self, chars) :
        mydict = {}
        
        for i in chars:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
              
        count = 0
        for char,freq in mydict.items():
            if freq > 1:
                count += 2
            else:
                count += 1
        chars.clear()
        l = []
        for char, freq in mydict.items():
            if freq > 1:
                l.append(char)
                if len(str(freq)) == 1:
                    l.append(str(freq))
                else:
                    for f in str(freq):
                        l.append(f)
            else:
                l.append(char)
        #print(l)
        chars[:len(l)] = l
        #print(chars)
        return count,chars
    
s = Solution()
print('Enter the elements in the list(a b b b b b b b b b b)')
chars = list(map(str,input().split()))
count,c = s.compress(chars)
print('Return value(count and chars): ',count, ' & ', c)     
      