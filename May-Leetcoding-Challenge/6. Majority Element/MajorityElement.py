#import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #n = floor(n/2)
        
        n = len(nums)//2
        mydict = {}
        
        for i in nums:
            if i in mydict:
                 mydict[i] += 1
            else:
                mydict[i] = 1
        
        for c,f in mydict.items():
            if f>n :
                return c
        