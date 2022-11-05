// https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ch=True
        def check(p,q):
            if p or q:
                nonlocal ch
                if (not p ) or  (  not q):
                    ch=False      
                if p.val!=q.val:
                    ch=False      
                check(p.left,q.left)
                check(p.right,q.right)
        check(p,q)
        return ch
                    
                #     return 0
                # if p.left and q.left :
                #   l=isSameTree(p.left,q.left)
                # if p.right and q.right :
                #   l=isSameTree(p.right,q.right)
                


        