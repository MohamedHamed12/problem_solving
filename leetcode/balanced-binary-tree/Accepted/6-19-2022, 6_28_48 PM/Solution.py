// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ch=True
        def path(root):
             
               if not root :
                  return 0
               nonlocal ch
               l=0;r=0
               if root.left:
                  l=path(root.left)
               if root.right:
                  r=path(root.right)
               if abs(l-r)>1:
                    ch=False
               return 1+max(l,r)
        path(root)
        
        return ch
        
                
        
        