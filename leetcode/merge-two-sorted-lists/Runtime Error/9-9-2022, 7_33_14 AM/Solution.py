// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, h: Optional[ListNode], k: Optional[ListNode]) -> Optional[ListNode]:
        # global k,h
        if h.val>k.val:
            head=ListNode(h.val)
            h=h.next
        else:
            head=ListNode(k.val)
            k=k.next
        tem=head
            
        def geth():
          nonlocal h,tem
          tem.next=ListNode(h.val)
          h=h.next
          tem=tem.next
        def getk():
          nonlocal k,tem
          tem.next=ListNode(k.val)
          k=k.next
          tem=tem.next
        while h or k:
           if h and k:
              if h.val<k.val:geth() 
              else:getk()
     
           elif h:
              while h:geth()
                  
           elif k:
              while h:getk()
                  
        return head

            
            
            
            
        
            
     
                
        return tem
            
            