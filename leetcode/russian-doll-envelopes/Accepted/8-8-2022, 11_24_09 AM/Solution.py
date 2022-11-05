// https://leetcode.com/problems/russian-doll-envelopes

class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        n=len(e)
        tem=[]
        e=sorted(e,key=lambda x:(x[0],-x[1]))
        
        for _,i in e:
            ind=bisect_left(tem,i)
            if ind>=len(tem): tem.append(i)
               
            else: tem[ind]=i
               
        return len(tem)
                                    
        # tot=0
        # a=0;b=0
        # e=sorted(e,key=lambda x:x[0])
        # for u,v in e:
        #     if u>a  and v>b:
        #         a,b=u,v
        #         tot+=1
        # return tot