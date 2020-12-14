# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:20:34 2020

@author: egayu
"""
import sys
class TreeNode:
     def __init__(self, val):
         self.val = val
         self.left = None
         self.right = None
         
def validatebst(root):
    #result = ['valid','not valid']
    def validate(root, MIN, MAX):
        if root is None:
            return True
        
        if root.val > MAX or root.val <= MIN:
            return False
        
        return validate(root.left, MIN, root.val) and validate(root.right, root.val, MAX)
    
    MIN, MAX = -sys.maxsize, sys.maxsize
    return validate(root, MIN, MAX)


#levelorder = [5,1,4,None,None,3,6]
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(10)
root.left.left = None
root.left.right = None

root.right.left = None
root.right.right = None

result = validatebst(root)
print('Valid?>>>> ',result)
