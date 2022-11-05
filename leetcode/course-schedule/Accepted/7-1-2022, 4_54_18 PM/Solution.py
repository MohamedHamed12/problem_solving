// https://leetcode.com/problems/course-schedule

from collections import defaultdict

class Solution:
    def canFinish(self,  n, l) :
            d=defaultdict(list)
            visit=set()
        
            for u , v in l :
                d[u].append(v)
                
            def dfs(num):
                if  d[num]==[]:return True
                if num in visit:return False
                visit.add(num)
                for i in d[num]:
                    if not dfs(i):return False
                visit.remove(num)
                d[num]=[]
                return True
            for i in range(n):
                if not dfs(i):return False 
                
                 
            return True    
                       
                     

