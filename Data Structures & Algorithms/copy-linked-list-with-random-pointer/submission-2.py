"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        My approach before conceptual 
        curr = head
        newHead = Node(curr.val) 
        curr2 = newHead 
        random = curr.random 
        while curr.next: 
            curr2.val = curr.val
            nxt = Node(0)
            curr2.random = random 
            curr2.next = nxt 
            curr2 = curr2.next 
            random = curr.next.random
            curr = curr.next
        curr2.val = curr.val 
        curr2.random = random  
        return newHead 
        """
        nodes = {None: None}
        curr = head 
        while curr: 
            nodes[curr] = Node(curr.val)
            curr = curr.next 
        
        
        curr = head 
        while curr:
            curr2 = nodes[curr]
            curr2.next = nodes[curr.next]
            curr2.random = nodes[curr.random] 
            curr = curr.next 
        return nodes[head]


                

        