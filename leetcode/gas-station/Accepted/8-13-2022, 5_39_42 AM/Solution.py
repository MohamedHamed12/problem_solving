// https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l=[]
        tmp=0
        tot=0
        mn=float('inf')
        for i in range(len(gas)):
            l.append(gas[i]-cost[i])
            tot+=gas[i]-cost[i]
            if mn>tot:
                mn=tot
                ind =i
        if tot<0:return -1
        else:return (ind+1)%len(gas)
            
            
        