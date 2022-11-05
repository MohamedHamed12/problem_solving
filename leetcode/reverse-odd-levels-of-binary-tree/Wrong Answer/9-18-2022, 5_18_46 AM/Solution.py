// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            q=[root]
            ind=1
            l=[]
            while q:
                tmp=[]
                while q:
                    i=q.pop(0)
                    if i:
                        tmp.append(i)
                        l.append(i)
                        q.append(i.left)
                        q.append(i.right)
                if ind%2==1:tmp=tmp[::-1]
                l.append(tmp)
                ind+=1
            r=TreeNode(l.pop(0))
            q=[r]
            while l:
                tmp=q.pop(0)
                if l:tmp.left=TreeNode(l.pop(0))
                if l:tmp.right=TreeNode(l.pop(0))
                q.append(tmp.left)
                q.append(tmp.right)
            return r
