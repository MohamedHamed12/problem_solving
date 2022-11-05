// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, r: Optional[TreeNode], queries: List[int]) -> List[int]:
        height,depth=defaultdict(deque),defaultdict(deque)
        def dfs(root ,h):
            if not root:return -1
            height[root.val]=h
            mx=max(dfs(root.left,h+1),dfs(root.right,h+1))+1
            depth[root.val]=mx
            return mx
        dfs(r,0)
        cousin=defaultdict(deque)
        for val ,h in height.items():
            cousin[h].append((depth[val],val))
            cousin[h].sort()
            if len(cousin[h])>2:cousin[h].pop(0)
        ans =deque()
        for q in queries:
            h=height[q]
            # ans.append(cousin[h])
            if len(cousin[h])==1:ans.append(h-1)
            elif cousin[h][1][1]==q:ans.append(h+cousin[h][0][0])
            else :ans.append(h+cousin[h][1][0])
        return ans
