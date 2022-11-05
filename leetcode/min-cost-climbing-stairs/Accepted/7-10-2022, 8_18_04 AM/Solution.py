// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        m=min(cost[0],cost[1])
        # cost[0],cost[1]=0,0
        for i in range(2,n):
            cost[i]=min(cost[i-2],cost[i-1])+cost[i]
        return min(cost[n-1],cost[n-2])
        # return (cost[n-2])