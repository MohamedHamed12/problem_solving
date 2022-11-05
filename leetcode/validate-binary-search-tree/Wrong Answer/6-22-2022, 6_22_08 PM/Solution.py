// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       l=[]
       def getnodes(root):
            nonlocal l
            if  root :
                 
        
                if root.left:
                    getnodes(root.left)
                l.append(root.val)
                if root.right:
                    getnodes(root.right)
      
       getnodes(root)
       if l==sorted(l):
          return True
       else :
            return False
#                 m =self.isValidBST(root.left)
             


#             if root.right:
#                 if root.right.val<=root.val:
#                     return False
#                 n=self.isValidBST(root.right)
#             m=n=True
#             if not root :
#                 return True
        
#             if root.left:
#                 if root.left.val>=root.val:
#                     return False
                    
#                 m =self.isValidBST(root.left)
             


#             if root.right:
#                 if root.right.val<=root.val:
#                     return False
#                 n=self.isValidBST(root.right)
               
#             return  m and n