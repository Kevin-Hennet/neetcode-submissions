# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def valid(root, subRoot): 
            if not root and not subRoot: 
                return True
            elif (not root or not subRoot) or (root.val != subRoot.val):
                return False 
            else: 
                left = valid(root.left, subRoot.left)
                right = valid(root.right, subRoot.right)
                return left and right 
        

        if not root:
            return False 
        elif root.val == subRoot.val:
            rootWalker = root
            subRootWalker = subRoot
            if valid(rootWalker, subRootWalker): 
                return valid(rootWalker, subRootWalker)
            else: 
                left = self.isSubtree(root.left, subRoot)
                right = self.isSubtree(root.right, subRoot)
                return left or right

        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right

        


        
        

        