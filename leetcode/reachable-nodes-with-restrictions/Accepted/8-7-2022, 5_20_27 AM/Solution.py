// https://leetcode.com/problems/reachable-nodes-with-restrictions

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        d=defaultdict(list)
        visit=[0 for i in range(n)]
        for u ,v in edges:
            d[u].append(v)
            d[v].append(u)
        for i in restricted:
            visit[i]=1
        q=[0]
        while q:
            root=q.pop(0)
            visit[root]=1
            for i in d[root]:
                if  visit[i]==0 and  i not in q:
                    q.append(i)
        return sum(visit)-len(restricted)