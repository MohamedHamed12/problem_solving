// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        l=[]
        tot=[]
        # tot.append([root.val])
        l.append(root)
        while len(l)>0:
            tem=[]
            temtot=[]
            for i in l:
                if i.left:
                   tem.append(i.left)
                if i.right:
                   tem.append(i.right)
                temtot.append(i.val)
            l=tem
            tot.append(temtot)
        return tot
        

            
        
        
        