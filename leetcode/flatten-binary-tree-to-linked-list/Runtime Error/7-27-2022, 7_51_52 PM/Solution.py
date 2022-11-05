// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tot=[]
        def dfs(root):
           
            if not root:return 
            tot.append(root)
            dfs(root.left)
            
            dfs(root.right)
        dfs(root)
        
        for i in range(len(tot)-1):
            tot[i].left=None
            tot[i].right=tot[i+1]
        root=tot[0]
        
                