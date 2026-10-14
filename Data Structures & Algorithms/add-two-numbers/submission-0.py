# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #my attempt oh my days I thought I had it smh
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
