// https://leetcode.com/problems/add-two-numbers

# class Solution:
#     def minMaxGame(self, nums) :

#         # x1=[]
#         # for i in nums:
#         #     if i%2==0:
#         if len(nums)==1:
#             # print(nums[0])
#             return nums[0]

#         x1=[]
#         tem=int(len(nums)/2)
#         for i in range(tem) :

#             if i%2==0:
#                 x1.append(min(nums[2*i],nums[2*i+1]))
#             else:
#                  x1.append(max(nums[2*i],nums[2*i+1]))
#         return self.minMaxGame(x1)
# # l=list(map(int,input().split()))
# # l=[1,3,5,2,4,8,2,2]
# # l=[3]
# while True:             # Loop continuously
#     inp = input() # Get the input
#     if inp == "":       # If it is a blank line...
#         break
#     l=list(int(i) for i in inp if  i.isdigit())
#     s=Solution()
#     print(s.minMaxGame(l))
# class Solution:
#     def partitionArray(self, nums, k):
#         nums = sorted(nums,reverse=True)
#         j = 0
#         tot = 1
#         for i in range(len(nums)):
#             if nums[j]-nums[i] <= k:
#                 pass
#             else:
#                 j = i
#                 tot += 1
#         return tot


# # l=list(map(int,input().split()))
# l = [3, 6, 1, 2, 5]
# s = Solution()
# print(s.partitionArray(l, 2))
# from operator import le


# class Solution:
# def arrayChange(self, nums, operations ) :
#     nums=sorted(nums);n=len(nums)
#     operations=sorted(operations);op=len(operations)
#     i=j=0
#     while i<n and j<op:
#         if nums[i]== operations[j][0]:
#             nums[i]=operations[j][1]
#             j+=1
#             i+=1
#         elif nums[i]> operations[j][0]:
#             j+=1
#         elif nums[i]<operations[j][0]:
#             i+=1
#     return nums


# l=[1,2,3,6,5]
# print(l.index(3))
# print(sorted( [[1,3],[8,7],[6,1]]))
# class Solution:
#     def arrayChange(self, nums, operations) :
#         d={}
#         for i ,j in reversed(operations) :
#             if j not in d:

#                 d[i]=j
#             else:
#                 i
# d = {}
# # l=[1,2,4,6]

# operations=[[1,3],[3,7],[6,1]]
# for s, e in reversed(operations):
# 		d[s] = d.get(e,e)
#         		# d[s] = d[e] if e in d else e

# print(d)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        tot1 = 0
        tot2 = 0
        n1 = 1
        n2 = 1
        while l1:
            tem = n1*l1.val
            tot1 += tem
            l1 = l1.next
            n1*=10
        while l2:
            tem = n2*l2.val
            tot2 += tem
            l2 = l2.next
            n2 *= 10
        tot1 += tot2
        return self.createlink(tot1)

    def createlink(self, tot1):
        # head = ListNode()
        # tem = head
        b = True
        for i in reversed(str(tot1)):
            if b:
                h = ListNode(int(i))
                tem = h
                b = False
            else:
                tem2 = ListNode(int(i))
                tem.next = tem2
                tem = tem2
        return h


s = Solution()
h = s.createlink(942)
m = s.createlink(9465)
t = s.addTwoNumbers(h, m)
# while h:
#     print(h.val)
#     h = h.next

while t:
    print(t.val, end="")
    t = t.next
print()
