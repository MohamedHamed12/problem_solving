// https://leetcode.com/problems/russian-doll-envelopes

class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        n=len(e)
        tem=[]
        e=sorted(e,key=lambda x:(x[0]))
        u,v=0,0
        tem1=0
        for i,j in e:
           
           if u<i and v<j:
                u,v=i,j
                tem1+=1
        e=sorted(e,key=lambda x:(x[1]))
        u,v=0,0
        tem2=0
        for i,j in e:
           
           if u<i and v<j:
                u,v=i,j
                tem2+=1
        return max(tem2,tem1)
                                 

                                    
        # tot=0
        # a=0;b=0
        # e=sorted(e,key=lambda x:x[0])
        # for u,v in e:
        #     if u>a  and v>b:
        #         a,b=u,v
        #         tot+=1
        # return tot