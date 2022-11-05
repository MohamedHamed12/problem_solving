// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, h: Optional[ListNode], k: Optional[ListNode]) -> Optional[ListNode]:
        if not h:return k
        if not k :return h
        head=ListNode()
        tem=head
  
        while h and k:
              if h.val<k.val:
                tem.next=ListNode(h.val)
                h=h.next
              else:
                 tem.next=ListNode(k.val)
                 k=k.next
              tem=tem.next
           
     
        while  h:
                tem.next=ListNode(h.val)
                h=h.next
                tem=tem.next
                  
        while  k:
                 tem.next=ListNode(k.val)
                 k=k.next
                 tem=tem.next
                  
        return head.next

            
            