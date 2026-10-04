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
        
        hashset = set()
        while head: 
            if head in hashset:
                return True 
            else: 
                hashset.add(head)
                head = head.next 
        return False
        """
        if head is None: 
            return False 
        s = head
        f = head.next  
        while f is not None and f.next is not None: 
            if s == f: 
                return True 
            
            s = s.next 
            f = f.next.next 
        return False  
        
