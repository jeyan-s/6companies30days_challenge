class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) 
    {
        int n = nums.size();
        vector<int> rslt, dp(n, 1);
        sort(nums.begin(), nums.end());
        for (int x = 0; x < n; x++)
            for (int y = 0; y < x; y++)
                if (nums[x] % nums[y] == 0)
                    dp[x] = max(dp[y] + 1, dp[x]);
        int length = *max_element(dp.begin(), dp.end());
        int last = -1;
        while (n--)
        {
            if (dp[n] == length)
            {
                if (rslt.empty()) 
                {
                    last = nums[n];
                    rslt.push_back(nums[n]);
                    length--;
                }
                else if (last % nums[n] == 0) 
                {
                    last = nums[n];
                    rslt.push_back(nums[n]);
                    length--;
                }
            }
        }
        return rslt;
    }

};
