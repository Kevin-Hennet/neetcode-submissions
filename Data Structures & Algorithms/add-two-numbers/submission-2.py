# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        my approach 
        n1 = ""
        n2 = ""
        while l1: 
            n1 += str(l1.val)
            l1 = l1.next
        while l2: 
            n2 += str(l2.val)
            l2 = l2.next 
        n1 = n1[::-1]
        n2 = n2[::-1]
        n1 = int(n1)
        n2 = int(n2)
        res = n1+n2
        res = str(res)
        res = res[::-1]
        reslst = ListNode()
        curr = reslst 
        for i in range(len(res) - 1):
            curr.val = int(res[i])
            curr.next = ListNode() 
            curr = curr.next
        curr.val = int(res[-1])    
        return reslst
        """ 
        #alt approach 
        dummy = ListNode()
        curr = dummy 
        carry = 0 
        while l1 or l2 or carry != 0: 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            
            # new digit 
            val = v1 + v2 + carry 
            carry = val // 10 
            val = val % 10 
            curr.next = ListNode(val)
            curr = curr.next 
            l1 = l1.next if l1 else None 
            l2  = l2.next if l2 else None 
        
        return dummy.next
        

