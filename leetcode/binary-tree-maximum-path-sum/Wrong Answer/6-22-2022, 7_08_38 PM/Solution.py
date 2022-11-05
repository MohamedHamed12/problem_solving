// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
       l=-10000
       def getnodes(root):
            nonlocal l
            if  root :
                 
                tot=0
                if root.left:
                    getnodes(root.left)
                if root.left:
                    tot+=root.left.val
                if root.right:
                    tot+=root.right.val
                tot+=root.val
                
                l=max(l,tot)
                if root.right:
                    getnodes(root.right)
      
       getnodes(root)
      
       return l
        