// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or

class Solution:
    def smallestSubarrays(self, l: List[int]) -> List[int]:
        tmp=[float('inf')]*32
        tot=[]
        mx=max(l)
        for i in range(len(l)-1,-1,-1):
            tot.append(1)
            for sft in range(mx.bit_length()+1):
                b=l[i]&(1<<sft)
                if b!=0:
                    tmp[sft]=i
                else:tot[-1]=max(tot[-1],tmp[sft]-i+1) if tmp[sft]!=float('inf') else tot[-1]
        return tot[::-1] 