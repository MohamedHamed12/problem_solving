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
            ind=0
            l=[]
            while q:
                tmp=[]
                t=[]
                while q:
                    i=q.pop(0)
                    if i:
                        tmp.append(i.val)
                        t.append(i.left)
                        t.append(i.right)
                q=t.copy()
                if ind%2==1:tmp=tmp[::-1]
                l.append(tmp)
                ind+=1
            l=sum(l,[])
            r=TreeNode(l.pop(0))
            q=[r]
            while l and q:
                t=[]
                while l and q:
                    tmp=q.pop(0)
                    if l:tmp.left=TreeNode(l.pop(0))
                    if l:tmp.right=TreeNode(l.pop(0))
                    t.append(tmp.left)
                    t.append(tmp.right)
                q=t.copy()
            return r
