# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #my attempt via recursive DFS 
        """
        if not root: 
            return 0 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """
        # Attempt with iterative BFS (just going to watch the video tbh)
        if not root: 
            return 0 
        level = 0 
        q = deque([root])
        while q: 
            for i in range(len(q)): 
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            level += 1 
        return level 
        # Iterative DFS 
        if not root: 
            return 0 
        stack = [(root, 1)]
        while stack: 
            for i in range(len(stack)): 
                node = stack.pop()
                if node[0].left: 
                    stack.append((node.left, node[1] + 1))
                if node[0].right: 
                    stack.append((node.right, node[1] + 1))
                res = nodes[0][1]
        return res 




          
         

        

        