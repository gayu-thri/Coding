# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:31:48 2020

@author: egayu
"""
class TreeNode():
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        

def ancestor(root, key):
    
    if root is None:
        return False
    
    if(root.val == key):
        return True
    
    x = ancestor(root.left, key)
    y = ancestor(root.right, key)
    
    if(x or y):
        print(root.val,end= " ")
        return True
    
    return False
            
            
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

key = 7
print("The ancestors of the key ",key," are: " )
print("\nAncestors exist: ", ancestor(root, key))