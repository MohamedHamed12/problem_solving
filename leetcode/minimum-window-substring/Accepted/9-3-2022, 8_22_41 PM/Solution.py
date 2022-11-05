// https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        n=len(s);n2=len(t)
        # if s==t:return s
        c=Counter(t)
        c2=Counter(s[:n2])
        ind=n2
        l=0
        tot=' '*n
        def check():
            for i in c:
                if  c[i]>c2[i]:return False
            return True
        
        while ind<n :
            while ind<n:
                if check():break
                c2[s[ind]]+=1
                ind+=1
            if check() and len(s[l-1:ind])<len(tot):tot=s[l:ind]
            while True:
                if not check():break
                elif len(s[l:ind])<len(tot):tot=s[l:ind]
                c2[s[l]]-=1
                l+=1
        if check() and n==n2:return s
        return tot if tot!=' '*n else ''
