# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        my attempt
        n = 0 
        while (head != None): 
            head.next
            n += 1
        for i in range() 
        reorder = head
        i = 0 
        count = 0  
        while i <= n:
        # this was so confusing i had to watch the video 
        s = head 
        f = head
        while f != None and f.next != None: 
            s = s.next
            prev = f.next 
            f = f.next.next
        s.next = None
        result.next = head
        while result.next != None:
            result.next = f
            f = prev
            result.next = head.next
        """
        slow = head
        fast = head.next 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        second = slow.next
        slow.next = None
        prev = None 
        while second:
            temp = second.next
            second.next = prev
            prev = second 
            second = temp 

        first = head
        second = prev
        while second: 
            temp1 = first.next
            temp2 = second.next 
            first.next = second 
            second.next = temp1
            first = temp1
            second = temp2 

        """
        my attempt at merging 
        while second.next: 
            temp = head.next
            secondTemp = second.next  
            head.next = second
            second.next = temp   
            head = temp 
            second = secondTemp 
        """


        

        

        

        

        
        
        
            
            
        
            
            