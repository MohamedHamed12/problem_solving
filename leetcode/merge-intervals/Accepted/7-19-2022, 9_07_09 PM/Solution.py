// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr=sorted(arr)
        l=deque()
        n=len(arr)
        
        # insort(arr,newInterval)
        l.append(arr.pop(0))
        while arr:
            x,y=arr.pop(0)
            if x>l[-1][1]:
                l.append([x,y])
            else:
                l[-1][1]=max(y,l[-1][1])
        return l