# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:20:34 2020

@author: egayu
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
def validatebst(root):
    #result = ['valid','not valid']
    
    
    left = root.left
    right = root.right
    
    if left and left.val > root.val:
            return "not valid"
    if right and right.val < root.val:
            return "not valid"
    res = validatebst(root.left) and validatebst(root.right)
    return res
'''
# ANOTHER METHOD 
import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate(root, MIN, MAX):
            
            if root is None:
                return True
            
            if root.val >= MAX or root.val <= MIN:
                return False
            
            return validate(root.left, MIN, root.val) and validate(root.right, root.val, MAX)
        
        MIN, MAX = -sys.maxsize, sys.maxsize
        return validate(root, MIN, MAX)
'''

#levelorder = [5,1,4,None,None,3,6]
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(None)
root.left.right = TreeNode(None)

root.right.left = TreeNode(None)
root.right.right = TreeNode(None)

result = validatebst(root)
print('Valid?>>>> ',result)
