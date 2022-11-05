// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tot=[]
        root=head
        ind=0
        while head:
            # tot.append(head)
            ind+=1
            head=head.next
        ind//=2
        for i in range(ind):
            root=root.next
        return root
        