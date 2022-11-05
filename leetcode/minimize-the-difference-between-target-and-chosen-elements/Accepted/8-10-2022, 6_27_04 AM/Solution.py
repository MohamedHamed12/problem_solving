// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        mask = 1
        for row in mat:
            next_mask = 0
            for num in row:
                next_mask |= (mask << num)
            mask = next_mask
        
        for deviation in count():
            for num in (target - deviation, target + deviation):
                if num >= 0 and mask & (1 << num):
                    return deviation
	    # m = len(mat)
	    # for i in range(m):
	    # mat[i].sort()
	    # q = set([0])
	    # for i in range(m):
	    # temp = set()
	    # for num1 in q:
	    # for num2 in mat[i]:
	    # temp.add(num1+num2)
	    # if(num1+num2 > target):
	    # break
	    # q = temp
	    # q = sorted(list(q))
	    # i = bisect_right(q, target)
	    # if(i == len(q)):
	    # return target - q[-1]
	    # if(i == 0):
	    # return q[0] - target
	    # return min(target-q[i-1], q[i]-target)
    
    
    
#         s=set([0])
#         ans=float('inf')
#         for i in l:
#             tem=set()
#             for j in i:
               
#                  for k in sorted(s):
#                     tem.add(k+j)
#                     if k+j >t :break
#             s=tem
#         for o in s:ans=min(ans,abs(o-t))
#         return ans