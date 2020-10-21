# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:43:15 2020

@author: egayu
"""

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

def symmetry(root):
    
    if(root is None):
        #A Tree with no node - symmetric
        return True
    
    def check(left, right):
        
        if left == None and right == None:
            return True
        
        if left == None or right == None:
            return False
        
        return (left.val == right.val and
                check(left.right, right.left) and
                check(left.left, right.right))
    
    return check(root.left, root.right)
    
def invert(root):
    
    if root is None:
        return root
    
    left = invert(root.left)
    right = invert(root.right)
    
    root.left = right
    root.right = left
    
    return root
    


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print("Symmetrical tree? ", symmetry(root))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Inversion of a tree", invert(root))