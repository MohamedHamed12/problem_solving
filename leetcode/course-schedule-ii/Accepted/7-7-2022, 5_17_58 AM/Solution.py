// https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       d={}
       for i in range(numCourses):
            d[i]=[]
       for u,v in prerequisites:
            d[u].append(v)
       # teml=[] 
       l=[]
       visit=set()
       
       def dfs(element):

         


          if d[element]==[]:
              if element not in l: l.append(element)
              return True
          if element in visit:return False
          visit.add(element)
          
          
          for item in d[element]:
                if not dfs(item):return False
          l.append(element)
         
          visit.remove(element)
          d[element]=[]
          return True
       for i in range(numCourses):
           if not dfs(i):return []
           # for j in teml:
           #    if j not in l:l.append(j)
           # teml.clear()
       return l