// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
#         mask = 1
#         for row in mat:
#             next_mask = 0
#             for num in row:
#                 next_mask |= (mask << num)
#             mask = next_mask
        
#         for deviation in count():
#             for num in (target - deviation, target + deviation):
#                 if num >= 0 and mask & (1 << num):
#                     return deviation


        reachable_sum = 1

        for row in mat:
            reachable_sum = reduce(lambda a, b: a | (reachable_sum << b), row, 0)
        min_diff = float("+inf")
        idx = 0
        while reachable_sum:
            if reachable_sum & 1:
                min_diff = min(min_diff, abs(target - idx))
            idx += 1
            reachable_sum >>= 1
        return min_diff
    
    
    
    
#         m = len(mat)
#         n = len(mat[0])
#         old_hash_set = set({0})
        
#         for i in range(m):
#             hash_set = set()
#             max_val = None
            
#             for elem in old_hash_set:
#                 row_sorted = sorted(mat[i])
#                 for row_val in row_sorted:
#                     if max_val is None and elem + row_val >= target:
#                         max_val = elem + row_val
#                         hash_set.add(elem+row_val)
#                     elif max_val is not None and elem + row_val >= max_val:
#                         # we can ignore this number, since it's difference with target 
#                         # will always be more
#                         continue
#                     else:
#                         hash_set.add(elem+row_val)
#             old_hash_set = hash_set
            
#         min_diff = float('inf')
#         for elem in hash_set:
#             if abs(elem - target) < min_diff:
#                 min_diff = abs(elem - target)
#         return min_diff
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