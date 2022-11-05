// https://leetcode.com/problems/longest-ideal-subsequence

class Solution {
public:
    int longestIdealString(string arr, int k) {
        int n=arr.length();
        int lis[n];
 
    lis[0] = 1;
 
    /* Compute optimized LIS values in
       bottom up manner */
    for (int i = 1; i < n; i++) {
        lis[i] = 1;
        for (int j = 0; j < i; j++)
            if (abs(int(arr[i]) )- int(arr[j])<=k && lis[i] < lis[j] + 1)
                lis[i] = lis[j] + 1;
    }
 
    // Return maximum value in lis[]
    return *max_element(lis, lis + n);
        
        
        
        
        
    }
};