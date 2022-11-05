// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, l: List[List[str]]) -> int:
        def vald(n,m,i,j):
            if i<n and i>=0:
                if j<m and j>=0:
                    if l[i][j] =="1":
                      if [i,j] not in visit:
                        
                         return True
            return False
        if not l or not l[0]:
            return 0
        tot=0    
        visit=[]
        n=len(l);m=len(l[0])
        for i in range(n):
            for j in range(m):
                if l[i][j]=="1" and [i,j] not in visit:
                    tot+=1
                    q=[];q.append([i,j])
                    while len(q)>0:
                        i,j=q.pop()
                       
                        if vald(n,m,i+1,j)  :
                             q.append([i+1,j]) 
                        if  vald(n,m,i,j+1)  :
                              q.append([i,j+1])  
                        if vald(n,m,i-1,j)  :
                             q.append([i-1,j]) 
                        if vald(n,m,i,j-1) :
                              q.append([i,j-1])  
                        visit.append([i,j])
                    
        return tot
        