// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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
       l=sorted(set(l))
       return l[k-1]
        