// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, l: List[List[str]]) -> int:
        if not l or not l[0]:
            return 0
        tot=0    
       
        n=len(l);m=len(l[0])
        visit=[[False]*m]*n
        def vald(i,j):
            nonlocal m,n,visit,l
            if i<n and i>=0:
                if j<m and j>=0:
                    if l[i][j] =="1":
                        if  visit[i][j]==False:
                        
                          return True
            return False
      
        for i in range(n):
            for j in range(m):
                if l[i][j]=="1" and  visit[i][j]==False:
                    tot+=1
                    q=[];q.append([i,j])
                    while len(q)>0:
                        tem=q.pop()
                        h=tem[0];k=tem[1]
                        if vald(h+1,k)  :
                             q.append([h+1,k]) 
                        if  vald(h,k+1)  :
                              q.append([h,k+1])  
                        if vald(h-1,k)  :
                             q.append([h-1,k]) 
                        if vald(h,k-1) :
                              q.append([h,k-1])  
                        visit[h][k]=True
      
        return tot
        