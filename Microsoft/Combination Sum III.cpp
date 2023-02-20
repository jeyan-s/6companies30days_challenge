class Solution {
public:
    void solve(int available, int digit, int target, int current,vector<vector<int>>& rslt, vector<int> candidate)
    {
        //cout << available << ' ';
        if (available == 0)
        {
            if (current == target && digit == 0)
            {
                //cout << current << ' ' << target << '\n';
                rslt.push_back(candidate);
                //for (vector<int> x: rslt)
                //for (int y: x) cout << y << ' ';
               // cout << '\n';
            }
            return;
        }
        if (available < 0 || digit < 0 || current > target) return;
        candidate.push_back(available);
        solve(available - 1, digit - 1, target, current + available, rslt, candidate);
        candidate.pop_back();
        solve(available - 1, digit, target, current, rslt, candidate);
    }
    vector<vector<int>> combinationSum3(int k, int n) 
    {
        int k_ = 9;
        if (k > n || k > 9 || (k_ * (k_ + 1)) / 2 < n) return {};
        //map<int, vector<int>> rslt;
        vector<vector<int>> rslt;
        solve(9, k, n, 0, rslt, {});
        return rslt;
    }
};
