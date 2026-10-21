# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #my attempt
        if not root: 
            return 0 
        elif root.left != None or root.right != None: 
            leftLength = 1 + self.maxDepth(root.left)
            rightLength = 1 + self.maxDepth(root.right)   
            res = max(leftLength, rightLength)
            return res 
        else: 
            return 1
        
        # after conceptual 
        

        