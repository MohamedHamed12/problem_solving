// https://leetcode.com/problems/xor-queries-of-a-subarray

class Solution:
    def xorQueries(self, arr: List[int], Q: List[List[int]]) -> List[int]:
            
            for i in range(len(Q)):
                Q[i].append(i)
            Q=sorted(Q)
            lft=0;rgt=0
            s=0
            rr=[0]*len(Q)
            for i in range(len(Q)):
                l,r,ind=Q[i]

                while rgt>r:
                   
                    s^=arr[rgt-1]
                    rgt-=1

                while rgt<=r:
                    s^=arr[rgt]
                    rgt+=1

                while lft<l:
                    s^=arr[lft]
                    lft+=1

                rr[ind]=s
            return(rr)



