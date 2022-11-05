// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tem=0
        num=0
        while l1!=None :
            tem+=l1.val*(10**num)
            num+=1
            l1=l1.next
        tem2=0
        num=0
        while l2!=None :
            tem2+=l2.val*(10**num)
            num+=1
            l2=l2.next
        r=str(tem+tem2)[::-1]
        head=ListNode(((r)[0]))
        tem=head
        for i in str(r)[1:]:
            tem.next=ListNode(int(i))
            tem=tem.next
            
        return head
        