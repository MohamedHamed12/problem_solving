// https://leetcode.com/problems/non-overlapping-intervals

class Solution:
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        l=deque()
        n=len(arr)
        arr=sorted(arr)
        l.append(arr.pop(0))
        while arr:
            x,y=arr.pop(0)
            if x>=l[-1][1]:
                l.append([x,y])
            # else:
            #     l[-1][1]=min(y,l[-1][1])
                # arr.insert(0,[l[-1][1],max(y,l[-1][1])])
        return n-len(l)
        