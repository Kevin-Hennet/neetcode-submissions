# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        without conceptual 
        curr = head
        while head.next != None: 
            if head.next == curr: 
                return True 
            else: 
                head = head.next
        return False
        (hashset method)
        hashset = set()
        while head: 
            if head in hashset:
                return True 
            else: 
                hashset.add(head)
                head = head.next 
        return False
        """
        # had to watch solution for this but i understand what i did wrong 
        s = head
        f = head 
        while f and f.next: 
            s = s.next 
            f = f.next.next 
            if s == f: 
                return True 
            
            
        return False  
        
