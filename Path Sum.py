# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:49:29 2020

@author: egayu
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:    #Tree has no nodes
            return False
        
        if not root.left and not root.right and root.val == sum:    #Tree has only root
            return True
        
        rem_sum = sum - root.val
        return self.hasPathSum(root.left, rem_sum) or self.hasPathSum(root.right, rem_sum)
