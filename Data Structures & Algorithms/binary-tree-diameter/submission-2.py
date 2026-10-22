# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #my attempt  
        #if not root: 
        #    return 0 
        #left_length = 1 + self.diameterOfBinaryTree(root.left)
        #right_length = 1 + self.diameterOfBinaryTree(root.right)
        #return left_length + right_length

        # after conceptual / video since I never had to do a nested function
        # and global var in these neetcode examples 

        # returns height
        self.res = 0  
        def dfs(curr): 
            if not curr: 
                return 0 
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res 



        