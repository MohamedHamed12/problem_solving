// https://leetcode.com/problems/course-schedule

from collections import defaultdict

class Solution:
    def canFinish(self,  n, l) :
            d=defaultdict(list)
            visit=[]
            q=[];qtot=[]
            for u , v in l :
                d[u].append(v)
            for i in range(n):
                if not d[i]:
                    continue
                q.append(i)
              
                while True:
                    h=q.pop()
                    qtot.append(h)
                    if h in visit:return False
                    visit.append(h)
                    if not d[h]:
                        for k in qtot:
                            d[k]=[]
                            visit.clear()
                        break
                    for tem in d[h]:
                       q.append(tem)
            return True 
#             d=defaultdict(list)
#             visit=set()
        
#             for u , v in l :
#                 d[u].append(v)
                
#             def dfs(num):
#                 if  not d[num]:return True
#                 if num in visit:return False
#                 visit.add(num)
#                 for i in d[num]:
#                     if not dfs(i):return False
#                 visit.remove(num)
#                 d[num]=[]
#                 return True
#             for i in range(n):
#                 if not dfs(i):return False 
                
                 
#             return True    
                       
                     

