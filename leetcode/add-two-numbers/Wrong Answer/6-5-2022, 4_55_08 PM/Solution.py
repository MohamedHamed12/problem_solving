// https://leetcode.com/problems/add-two-numbers


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        tot1 = 0
        tot2 = 0
        n = 10
        while l1:
            tot1 *= n
            tot1 += l1.val
            l1 = l1.next
        while l2:
            tot2 *= n
            tot2 += l2.val
            l2 = l2.next
        tot1 += tot2
        return self.createlink(tot1)

    def createlink(self, tot1):
        # head = ListNode()
        # tem = head
        b = True
        for i in reversed(str(tot1)):
            if b:
                head = ListNode(int(i))
                tem = head
                b = False
            else:
                tem2 = ListNode(int(i))
                tem.next = tem2
                tem = tem2
        return head