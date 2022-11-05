// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
     
        tot=0
        mn=float('inf')
        for i in range(len(gas)):
            tot+=gas[i]-cost[i]
            if mn>tot:
                mn=tot
                ind =i
        if tot<0:return -1
        else:return (ind+1)%len(gas)
            
            
        