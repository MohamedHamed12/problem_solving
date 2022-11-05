// https://leetcode.com/problems/course-schedule

from collections import defaultdict

class Solution:
    def canFinish(self,  n, l) :
            d=defaultdict(list)
            visit=[True]*(n)
            q=[]
            for u , v in l :
                d[u].append(v)
            for i in range(n):
             if d[i]:
                
                if visit[i]: q.append(i)
                # visit[i]=False
    
                while q:
                    k=q.pop()
                    for h in d[k]:
                        if not d[h] :continue
                        if visit[h]:return False
                        q.append(h)
                    visit[k]=False
                       
                     
            return True     

