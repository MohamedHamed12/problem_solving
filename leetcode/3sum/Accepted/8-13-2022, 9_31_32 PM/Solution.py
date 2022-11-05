// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, l: List[int]) -> List[List[int]]:
          l=sorted(l)
          tmp=[]
          for i,a in enumerate((l)):
                if i>0 and l[i]==l[i-1]:continue
                lft=i+1; r=len(l)-1
                while lft<r:
                
                    s=l[i]+l[lft]+l[r]
                    if s>0:r-=1
                    elif s<0:lft+=1
                    else:
                        tmp.append([l[i],l[lft],l[r]])
                        lft+=1
                        while l[lft]==l[lft-1] and lft<r:lft+=1
          return tmp