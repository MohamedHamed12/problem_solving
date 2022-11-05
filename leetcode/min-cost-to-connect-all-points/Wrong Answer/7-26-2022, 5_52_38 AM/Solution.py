// https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution(object):
    def minCostConnectPoints(self, points):
        class sol:
            def __init__(self,n ):
                self.parent=[i for i in range(n+1)]
                self.rank=[0]*(n+1)
                self.totalW=0
            def find (self,x):
                if x!=self.parent[x]:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
            def union (self,x,y):
                xroot=self.find(x)
                yroot=self.find(y)
                if xroot==yroot:return
                if self.rank[xroot]==self.rank[yroot]:
                    self.parent[xroot]=yroot
                    self.rank[yroot]+=1
                elif self.rank[xroot]>self.rank[yroot]:
                    self.parent[yroot]=xroot
                else:
                    self.parent[xroot]=yroot
            def kruskals(self,l):
                l.sort(key=lambda x: x[2])
                for u,v,w in l:
                    if self.find(u)==self.find(v):
                        continue
                    else:
                        self.union(u,v)
                        self.totalW+=w
                return self.totalW

        s=sol(len(points))
        l=[]
        for u,p1 in enumerate(points):
            for  v,p2  in enumerate(points):
                x1,y1=p1
                x2,y2=p2
                dis=abs(x1-x2+y1-y2)
                l.append([u,v,dis])
        res = s.kruskals(l)
        return res
