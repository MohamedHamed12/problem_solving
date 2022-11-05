// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        
        return 1+self.goodnum(root,root.val)
    def goodnum(self,root ,x):
            if not root :
                return 0 
            m=0;n=0
            if root.left:
                if root.left.val>=x:
                    
                    m =1+self.goodnum(root.left,root.left.val)
                else:
                    m +=self.goodnum(root.left,x)


            if root.right:
                if root.right.val>=x:
                   
                    n=1+self.goodnum(root.right,root.right.val)
                else:
                    n+= self.goodnum(root.right,x)

            return m+n