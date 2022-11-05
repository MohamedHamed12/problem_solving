// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, p: List[int]) -> int:
        n=len(p)
        mx=-float('inf')
        l=r=p[0]
        for i in range(n):
            if p[i]<l:l=r=p[i]
            if p[i]>r:
                r=p[i]
                mx=max(mx,r-l)
        return mx
#         s=set()
#         mx=-float('inf')
#         j=0
#         ps=sorted(ps[-1],reverse=True)
#         for i in p:
#             while i==ps[j] or :j+=1
                
            
            
        
        