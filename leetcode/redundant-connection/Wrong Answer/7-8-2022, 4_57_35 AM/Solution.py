// https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       d=defaultdict(list)
       visit=set()
       loop=set()
       for u,v in edges:
            d[u].append(v)
            d[v].append(u)
       def dfs(root):
          q=[root]
          while q:
                temroot=q.pop(0)
                tem=set()
                for i in d[temroot]:
                    if len(tem)==2:return [temroot,i]
                    if i in visit: tem.add(i)
                    if i in q:return [temroot,i]
                    else:q.append(i)
                visit.add(temroot)
          return [-1]
       for i,j in edges:
            if i not in visit:
                m= dfs(i)
                if m!=[-1]:return m
       return [-1]





# if element in loop:return element
          # if element in visit:return -1
          # loop.add(element);visit.add(element)
          # for child in d[element]:
          #       if dfs(child):return  [element,child]
          # loop.remove(element)
          # return False