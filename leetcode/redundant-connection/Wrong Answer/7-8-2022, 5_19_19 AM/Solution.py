// https://leetcode.com/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit=set();l=[]
        for i,j in edges:
            if i in visit and j in visit:
                l.append([i,j])
            else:
                visit.add(i);visit.add(j)
        return l[-1]
#        d=defaultdict(list)
#        visit=set()
#        loop=set()
#        for u,v in edges:
#             d[u].append(v)
#             d[v].append(u)
       
#        def dfs(root):
       
                
#        for i,j in edges:
#             if i not in visit:
#                 m= dfs(i)
#                 if m!=[-1]:return m
#        return [-1]
#  # if root in visit
#  #        visit.add(root)
#  #            for i in d[root]:
#  #                if i in visit:continue
#  #                tem.append(root)
#  #                dfs(i)
#  #                tem.remove(root)

# # temroot=q.pop()
# #                 tem=set()
# #                 for i in d[temroot]:
# #                     if len(tem)==2:return [temroot,i]
# #                     if i in visit: tem.add(i)
# #                     else:q.append(i)
# #                 visit.add(temroot)
# #           return [-1]


# # if element in loop:return element
#           # if element in visit:return -1
#           # loop.add(element);visit.add(element)
#           # for child in d[element]:
#           #       if dfs(child):return  [element,child]
#           # loop.remove(element)
#           # return False