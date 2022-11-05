// https://leetcode.com/problems/two-sum

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>r;
                for (int i=0;i<nums.size();i++)
                {
                        for (int j=0;j<nums.size();i++)
                    {
                        if (nums[i]+nums[j]==target)
                        {
                            r.push_back(i);
                            r.push_back(j);
                            return r;
                        }
                        
                    }
                }

    }
};