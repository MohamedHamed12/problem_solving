// https://leetcode.com/problems/course-schedule

from collections import defaultdict

class Solution:
    def canFinish(self,  n, l) :
            d=defaultdict(list)
            visit=[True]*(n)
            q=[];qtem=[]
            for u , v in l :
                d[u].append(v)
            for i in range(n):
             if d[i]:
                if visit[i]: 
                    q.append(i)
                    qtem.append(i)
                else:continue    
                while q:
                    k=q.pop()
                    for h in d[k]:
                        if d[h]:
                          if h in  qtem:return False
                        if not visit[h]:continue
                        if not d[h] :
                             visit[h]=False
                        
                        q.append(h)
                        qtem.append(h)     
                for item in qtem:
                    visit[item]=False
                qtem.clear()
                            
            return True    
                       
                     

