// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, l: List[List[str]]) -> int:
        def vald(n,m,tem):
            if tem[0]<n and tem[0]>=0:
                if tem[1]<m and tem[1]>=0:
                   return True
        tot=0    
        visit=[]
        n=len(l)
        m=len(l[0])
        for i in range(n):
            for j in range(m):
                if  [i,j] not in visit:
                    tot=1
                    q=[[i,j]]
                    while q:
                        tem=q.pop(0)
                        if vald(m,n,tem):
                           q.append([tem[0]+1,tem[1]])
                           q.append([tem[0],tem[1]+1])
                        visit.append(tem)
                    
        return tot
        