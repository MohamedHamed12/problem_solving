// https://leetcode.com/problems/redundant-connection

from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edags: List[List[int]]) -> List[int]:

            l=[]
            maxnum=max([max(i) for i in edags ])

            d=defaultdict(list)
            def unoin(x,y,parent):
                    parent[x]=y


            def find(parent,x):
                   if parent[x]==-1:return x
                   elif  x==parent[x]:return x

                   else: return find(parent,parent[x])
            def check():
                     parent=[-1]*(maxnum+1)
                     for i ,j in edags:
                            x=find(parent,j)
                            y=find(parent,i)
                            if x==y:
                                l.append([i,j])
                            unoin(x,y,parent)
                     return l[-1]




            return check()