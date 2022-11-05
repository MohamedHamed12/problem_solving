// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) :
        l=0
        def path(root,l):
            if root :
                lf=0;rg=0
                if root.left :
                    lf=path(root.left,l)
                if root.right:
                    rg=path(root.right,l)
                l=max(l,(lf+rg+1))
                return 1+max(lf,rg)
                
            else:
                return 0
        return path(root,l)