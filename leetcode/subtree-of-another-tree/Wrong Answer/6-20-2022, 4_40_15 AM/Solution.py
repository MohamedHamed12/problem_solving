// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ch=False
        def check(root,subRoot):
            # if root or subRoot:
                if not (root and  subRoot ):
                    ch =False
                    return
                if root.val != subRoot:
                    ch =False
                    return
                if root.left  or subRoot.left :
                    path(root.left)
                if  root.right or  subRoot.right:
                    path(root.right)
            # else:
            #     ch=False
            #     return
                
                
        def path(root,subRoot):
            nonlocal ch
            # nonlocal check
            if ch :
                return
            if not root:
                return
            if root.val==subRoot.val:
                
                ch=True
                check(root,subRoot)
                if ch :
                    return 
            path(root.left,subRoot)
            path(root.right,subRoot)
        path(root,subRoot)
        return ch
        