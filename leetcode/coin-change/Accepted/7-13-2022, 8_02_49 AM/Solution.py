// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, l,n) :
          l=sorted(l)
          if n==0:return 0
          tot=[float('inf')]*(n+1) 
          for i in l:
            for j in range(n+1):

                if j<i:continue
                elif i==j:tot[j]=1
                else:tot[j]=min(tot[j],1+tot[j-i])
          return tot[-1] if tot[-1]!=float('inf') else -1
        # l=sorted(l)
        # tot=0
        # for i in l[::-1]:
        #     tot+=c//i
        #     c=c%i
        #     if c==0:return tot
        # if c==0:return tot
        # else:return -1