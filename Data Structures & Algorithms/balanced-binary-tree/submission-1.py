# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        my attempt before conceptual 
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return abs(left - right)
            
        if not root: 
            return True
        balanced = dfs(root)
        if balanced == 0 or balanced == 1: 
            return True
        else: 
            return False 
        """
        # after conceptual / video solution 
        def dfs(root): 
            if not root: 
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]




        
        