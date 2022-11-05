// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, r: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def rec(root):
            if root in [p,q]:return root
            l,r=rec(root.left),rec(root.right)
            if l and r: return root
            if l or r:return l or r
        return rec(r)
        
#         tem=[p,q]
#         ans
        
#         def rec
#         if not root: return 
#         if root.val==p :
  
#         if root.val==q
#         else:
#             self.rec(root.left)
#             self.rec(root.left)
#         if root.val==p : 
#            if self.rec(root.left,q) or self.rec(root.right,q):return self.val
#         else:root.val==p : 
            
#             if self.rec(root.left,q) or self.rec(root.right,q):return self.val
            