// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
         while root:
            tem=root.val 
            if  tem >p.val  and tem >q.val:
                root=root.left
            elif    tem <p.val and tem <q.val:
                root=root.right
            else:
                return root
            
        