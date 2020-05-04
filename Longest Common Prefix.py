# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:44:22 2020

@author: egayu
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        #minimum = min(strs, key=len) #finds shortest
        minimum = len(strs[0])
        for s in strs:
            minimum = min(len(s), minimum)
        lcp = ""    
        j = 0
        while(j < minimum):
            ch = strs[0][j]
            for i in range(len(strs)):
                if strs[i][j] != ch:
                    return lcp
            lcp = lcp + ch
            j = j + 1
            
        return lcp      
            
s = Solution()
strs = list(map(str,input('Enter the string array\n').split(',')))
res = s.longestCommonPrefix(strs)
print('LCP:', res)