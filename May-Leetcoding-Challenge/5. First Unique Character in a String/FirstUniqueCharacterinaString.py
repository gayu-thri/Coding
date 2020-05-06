class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        mydict = {}     #char: freq
        for char in s:
            if char in mydict:
                mydict[char] += 1
            else:
                mydict[char] = 1
                
        for char,freq in mydict.items():
            if freq == 1:
                return s.index(char)
            
        return -1
        
        