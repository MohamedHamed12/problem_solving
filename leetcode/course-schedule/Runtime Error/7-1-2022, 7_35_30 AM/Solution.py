// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, l: List[List[int]]) -> bool:
            d=defaultdict(int)
            n=len(l)
            visit=[True]*(n)
            for u , v in l :
                d[u]=v
                # d[v]=u
            for i in d:
                h=d[i]
                if not visit[h]:
                    continue
               
                q=[i]
                visit[h]=False
    
                    
                while True:
                        if h not in d:break
                        if d[h] not in q:
                            q.append(d[h])
                            visit[d[h]]=False
                        else:return False
                        h=d[h]
                     
            return True     
