# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:25:25 2020

@author: egayu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True     #tree with no node is symmetric
        
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            
            return left.val == right.val and check(left.right, right.left) and check(left.left, right.right)
        
        return check(root.left, root.right)
        
        