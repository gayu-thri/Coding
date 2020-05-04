# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:37:35 2020

@author: egayu
"""

class Solution:
    def TwoSum(self, nums, target):
        """
        :rtype: List[int]
        """
        # No duplicate elements
        result = []
        mydict = {}
        
        for i in range(len(nums)):
            mydict[nums[i]] = i
        print(mydict)
        for i in range(len(nums)):
            
            remaining = target - nums[i]
            if remaining in mydict.keys() and mydict[remaining] != i:
                return [i,mydict[remaining]]
s = Solution()
print('----TWO SUM---')
print("Enter the elements of the array")
nums = list(map(int,input().split()))
target = int(input(("Enter the target sum")))
out = s.TwoSum(nums,target)
print(out)
