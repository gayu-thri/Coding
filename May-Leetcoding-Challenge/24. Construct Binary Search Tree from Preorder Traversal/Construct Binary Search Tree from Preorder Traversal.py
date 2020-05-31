# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        # preorder -> root,left,right
        
        inorder = sorted(preorder)  #inorder - ascending order
        return self.constructbst(preorder, inorder)
    
    def constructbst(self, preorder, inorder):
        lenpre = len(preorder)
        lenin = len(inorder)
        
        if lenpre == 0:
            return None
        
        root = TreeNode(preorder[0])   
        rootindex = inorder.index(root.val)
        
        root.left = self.constructbst(preorder[1:rootindex+1], inorder[ :rootindex])
        
        root.right = self.constructbst(preorder[rootindex+1: ], inorder[rootindex+1: ])
        return root