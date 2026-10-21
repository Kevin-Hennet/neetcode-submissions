# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #my attempt via recursive DFS 
        if not root: 
            return 0 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # Attempt with iterative BFS (just going to watch the video tbh)
        if not root: 
            return 0 
        nodes = [root]
        level = 1 
        while len(nodes) != 0: 
            if nodes[0].left: 
                nodes.append(nodes[0].left)
            elif nodes[0].right: 
                nodes.append(nodes[0].right)
            nodes.pop()
            level += 1 
        return level 

          
         

        

        