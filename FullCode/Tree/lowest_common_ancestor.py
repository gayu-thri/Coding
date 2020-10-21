# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:51:56 2020

@author: egayu
"""

class Node():
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

def lca(root, n1, n2):
    
    if(root is None):
        return None
    
    if(root.val == n1 or root.val == n2):
        return root
    
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)
    
    if(left != None or right != None):
        return root
    
    if(left == None and right == None):
        return None
    
    if left != None:
        return left
    else:
        return right
    
    
    
'''
               1     - 2 return values
        r2       r3
         2          3
null         r5
    4      5     6     7
    
    (3,5)
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res = lca(root, 3, 5).val
print("LCA of 3 and 5: ", res)
    