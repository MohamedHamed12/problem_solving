// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ch=False
class Solution:
     def isSubtree(self, root, subRoot) :
            
            if not subRoot :return True 
            if not root :return False
            
            if root.val==subRoot.val:
                if  self.check(root,subRoot)==True :
                    return True 
                
           
            o =self.isSubtree(root.left,subRoot)
           
            p =self.isSubtree(root.right,subRoot)
            return o or p
            
     def check(self,r,s):
        if r or s :
            m=True;n=True
            if not (r and s):
                return False
            if r.val!=s.val:
                return False
            # if r.left or s.left:
            m= self.check(r.left,s.left)
            # if r.right or s.right:
            n= self.check(r.right,s.right)
            return m and n
        else :
           return True
            
#    
#             global ch
#             if not subRoot:
#                 ch= True
#                 return 
#             if not  root : 
#                 ch= False
#                 return
#             self.path(root,subRoot)
#             return ch 
#     def ccheck(self,root,subRoot):
#                 global ch
#                 # if ch : return
#                 if not (root and subRoot  ):
                    
#                     ch =False
#                     return
#                 if root.val != subRoot.val:
#                     ch =False
#                     return
#                 if  subRoot.left or root.left :
#                     self.ccheck(root.left,subRoot.left )
#                 if   subRoot.right or root.right:
#                     self.ccheck(root.right,subRoot.right)
    
#     def path(self,root,subRoot):
#             global ch
#             if ch :
#                 return 
          
#             if root.val==subRoot.val :
                
#                 ch=True
#                 self.ccheck(root,subRoot)
#                 if  ch :
#                      return 
#             if root.left:
#                 self.path(root.left,subRoot)
#             if root.right:
#                 self.path(root.right,subRoot)
            
         
        
        
        