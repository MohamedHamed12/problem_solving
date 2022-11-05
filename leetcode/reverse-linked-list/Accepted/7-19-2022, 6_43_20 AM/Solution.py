// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
            
            
        # while l:
        #     h=Node(i)
        #     h.next=node(i)
        if not l:return 
        h=root=ListNode(l[-1])
        for i in reversed(l[:-1]):
           h.next=ListNode(i)
           h=h.next
        return root
            
            
        