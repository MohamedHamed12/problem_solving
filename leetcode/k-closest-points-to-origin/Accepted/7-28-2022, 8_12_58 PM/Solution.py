// https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         d=deque()
#         tem=[]
#         def dis(x,y):
#             m= math.sqrt(x*x+y*y)
#             return m
#         for u,v in points:
#             insort(d,[dis(u,v),u,v])
#         for i in range(k):
#             del d[i][0]
#             tem.append(d[i])
#         return tem
        points.sort(key = lambda x: x[0] * x[0] + x[1] * x[1])
        return points[:k]