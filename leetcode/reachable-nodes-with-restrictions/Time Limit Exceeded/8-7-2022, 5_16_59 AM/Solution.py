// https://leetcode.com/problems/reachable-nodes-with-restrictions

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        d=defaultdict(list)
        visit=set()
        for u ,v in edges:
            d[u].append(v)
            d[v].append(u)
        q=[0]
        while q:
            root=q.pop(0)
            visit.add(root)
            for i in d[root]:
                if i not in visit and i not in restricted and i not in q:
                    q.append(i)
        return len(visit)