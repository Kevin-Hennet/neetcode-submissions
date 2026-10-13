# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        my attempt 
        count = 0
        curr = head  
        while curr: 
            curr = head
            head = head.next 
            count += 1
        position = count - n 
        newHead = ListNode()
        curr2 = newHead 
        for i in range(position - 1): 
            curr2.next = head 
            head = head.next 
        curr2.next = head.next 
        if head: 
            curr2.next = head 
        return newHead.next 
        """
        dummy = ListNode() 
        l = dummy
        l.next = head 
        r = head 
        for i in range(n): 
            r = r.next 
        while r: 
            l = l.next 
            r = r.next
        l.next = l.next.next 
        return dummy.next 
        
        
        
            
             

            
    