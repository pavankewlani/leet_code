class Solution {
public:
    int smallestUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        int low = 1, high = n, ans = n;
        long long base1 = 1315423911LL, mod1 = 1000000007LL;
        long long base2 = 2654435761LL, mod2 = 1000000009LL;
        auto hasUnique = [&](int len) -> bool {
            long long h1 = 0, h2 = 0;
            long long p1 = 1, p2 = 1;
            for (int i = 0; i < len - 1; ++i) {
                p1 = (p1 * base1) % mod1;
                p2 = (p2 * base2) % mod2;
            }
            unordered_map<long long, int> freq;
            freq.reserve(n - len);
            for (int i = 0; i < n; ++i) {
                if (i >= len) {
                    h1 = (h1 - (nums[i - len] * p1) % mod1 + mod1) % mod1;
                    h2 = (h2 - (nums[i - len] * p2) % mod2 + mod2) % mod2;
                }
                h1 = (h1 * base1 + nums[i]) % mod1;
                h2 = (h2 * base2 + nums[i]) % mod2;
                if (i >= len - 1) {
                    long long combined = (h1 << 32) | h2;
                    freq[combined]++;
                }
            }  
            for (auto& entry : freq) {
                if (entry.second == 1) return true;
            }
            return false;
        };
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (hasUnique(mid)) {
                ans = mid;
                high = mid - 1;
            } 
            else low = mid + 1;
        }
        return ans;
    }
};