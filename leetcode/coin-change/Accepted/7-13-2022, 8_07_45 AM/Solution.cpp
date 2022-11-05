// https://leetcode.com/problems/coin-change

class Solution {
public:
    int coinChange(vector<int>& coins, int am /*amount*/) 
    {
        vector<int> dp(am+1, INT_MAX-1);
        dp[0] = 0;
        for(int i=1; i<=am; ++i)
        {
            for(auto& c: coins)
            {
                if(i-c<0)
                {
                    continue;
                }
                if(dp[i-c] == INT_MAX-1) continue;
                dp[i] = min(dp[i], dp[i-c] + 1);
            }
        }
        return dp[am] == INT_MAX -1 ? -1 : dp[am];
    }
};