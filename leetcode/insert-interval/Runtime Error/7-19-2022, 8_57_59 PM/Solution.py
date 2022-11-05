// https://leetcode.com/problems/insert-interval

from bisect import insort

class Solution:
    def insert(self, arr: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l=deque
        n=len(arr)
        insort(arr,newInterval)
        l.append(arr.pop(0))
        while arr:
            x,y=arr.pop(0)
            if x>l[-1][1]:
                l.append([x,y])
            else:
                l[-1][1]=max(y,l[-1][1])
        return l
        
            
        
#         x,y=newInterval
#         n=len(intervals)
#         tem=[]
#         for  i in range(n):
#             if l[i][0]>=x:
#                 l[i][0]=x
                
                
#             elif l[i][1]>=x:
#                  l[i][1]=x
                
#                     for j in range(i+1,n):
#                         if l[i][0]>=y:
#                             tem.append([l[i][0],y)
#                             tem+=intervals[j+1:]
#                             break
                
#                         elif l[i][1]>=x:
                            
#                            tem.append([l[i][0],l[j][1]])
#                            tem+=intervals[j+1:]
#                            break
                        
#                  l[i+1][0]
                
                
#           tem.append(l[i])