// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
l=0
class Solution:
    def diameterOfBinaryTree(self, root) :
        
         def path(root):
            if root :
                global l
                lft=0;rg=0
                if root.left :
                    lft=path(root.left)
                if root.right:
                    rg=path(root.right)
                l=max(l,lft+rg+1)
                return 1+max(lft,rg)
                
            else:
                return 0
         m=path(root)
         return l-1