// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
            m=n=True
            if not root :
                return True
        
            if root.left:
                if root.left.val>=root.val:
                    return False
                    
                m =self.isValidBST(root.left)
             


            if root.right:
                if root.right.val<=root.val:
                    return False
                n=1+self.isValidBST(root.right)
               
            return  m and n