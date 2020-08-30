# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:06:37 2020

@author: egayu
"""

class Solution:
    def isValid(self, s: str) -> bool:
        #s = "([])"
        stack = []
        
        mapping = {')':'(', ']':'[', '}':'{'}
        
        for ch in s:
        
            if ch in mapping:
                
                if stack:
                    top = stack.pop()
                else:
                    top = '#'
                    
                if mapping[ch] != top:
                    return False
            
            else:
                stack.append(ch)
            
        return len(stack) == 0
            
s = Solution()
res = s.isValid("([({})])")            
print('The parantheses is valid: ',res)   