// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, n: int, lst: List[List[int]]) -> List[int]:
        # if not lst:return []
    
        graph=defaultdict(list)
        for u,v in lst:
            graph[v].append(u)
        def detect():
           visit=[False]*n
           stack=[False]*n
           def util(u):
               visit[u] = True
               stack[u]=True
               for v in graph[u]:
                   if not visit[v]:
                       if util(v):return True
                   if stack[v]:return True

               stack[u] = False

           for i in range( n):
               if not visit[i]:
                   if util(i) :return True
           return False


        if detect():return []
    
        def topologicalSort():
             visit=[False]*n
             stack=[]
             def util(u):
                visit[u] = True
                for v in graph[u]:
                    if not  visit[v]:util(v)
                stack.append(u)


             for i in range(n):
                    if not visit[i]:util(i)
             return stack[::-1]
        return   topologicalSort()

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#        d={}
#        for i in range(numCourses):
#             d[i]=[]
#        for u,v in prerequisites:
#             d[u].append(v)
#        l=[]
#        visit=set()
       
#        def dfs(element):

         


#           if d[element]==[]:
#               if element not in l: l.append(element)
#               return True
#           if element in visit:return False
#           visit.add(element)
          
          
#           for item in d[element]:
#                 if not dfs(item):return False
#           l.append(element)
         
#           visit.remove(element)
#           d[element]=[]
#           return True
#        for i in range(numCourses):
#            if not dfs(i):return []
#            # for j in teml:
#            #    if j not in l:l.append(j)
#            # teml.clear()
#        return l
