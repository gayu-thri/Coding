# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:54:32 2020

@author: egayu
"""
class Solution:
    def SortedSquares(self, A):
        """
        :type nums: List[int]
        """
        for i in range(0,len(A)):
            #A[i] = A[i]**2
            A[i] = A[i] * A[i]
        A.sort()
        return A


s = Solution()
print('----SORTED SQUARES---')
print("Enter the elements of the array")
nums = list(map(int,input().split()))
print("The sorted squares: ")
out = s.SortedSquares(nums)
print(out)
