// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, l: List[List[int]]) -> int:
        n=len(l)
        m=len(l[0])
        visit=[[True]*m for i in range(n)]
        tot=0
        # def check(i,j):
        #     if i<n and j< m and l[i][j]==1 and visit[i][j] :
        #           up=  check(i+1,j)
        #           down= check(i-1,j)
        #           left=  check(i,j+1)
        #           right= check(i,j-1)
        #           return 1+up+down+left+right
        #     else:
        #         return 0
        def valid(i,j):
            if i<n and i>=0 and j>=0 and j< m and l[i][j]==1 and visit[i][j]:return True
            return  False
        def check(h,k):
                if not  valid(h,k):
                    return
                tem=0
                nonlocal tot 
                t=[];t.append([h,k])
                while t:
                    i,j=t.pop(0)
                    if valid(i+1,j) and ([i+1,j] not in t):t.append([i+1,j])
                    if valid(i-1,j) and ([i-1,j] not in t):t.append([i-1,j])
                    if valid(i,j+1) and ([i,j+1] not in t):t.append([i,j+1])
                    if valid(i,j-1) and ([i,j-1] not in t):t.append([i,j-1])
                    visit[i][j]=False
                    tem+=1
                tot=max(tot,tem)
    
            
            
         
            
            
        for i in range(n):
            for j in range(m):
                check(i,j)
                     
        return tot
                