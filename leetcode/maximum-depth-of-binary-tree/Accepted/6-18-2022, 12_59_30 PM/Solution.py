// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            m=1;n=1
            if not root:
                return 0
        
            if root.left:
              m= 1+self.maxDepth(root.left) 
            if root.right:
              n= 1+self.maxDepth(root.right) 
            return max (m,n)
         
        