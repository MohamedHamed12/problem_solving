// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod=7+10**9
        n=len(hats)
        dic=defaultdict(list)
        for ind,lsthat in enumerate(hats):
            for hat in lsthat:
                dic[hat].append(ind)
        dp={}
        def rec(mask,h):
            if mask+1==1<n:return 1
            if h>40:return 0
            if (mask,h) in dp:return dp[(mask,h)]
            cnt=rec(mask,h+1)
            for p in dic :
                if (1<<p)&mask==0:cnt+=rec(mask|(1<<p),h+1)
            dp[(mask,h)]=cnt%mod
            return dp[(mask,h)]
        return rec(0,1)
        