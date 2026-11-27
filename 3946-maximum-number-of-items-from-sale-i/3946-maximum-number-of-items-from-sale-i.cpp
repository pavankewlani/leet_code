class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        vector<int> freeCount(n, 0);
        int minPrice = items[0][1];
        for (int i = 0; i < n; i++) {
            minPrice = min(minPrice, items[i][1]);
            for (int j = 0; j < n; j++) {
                if (i != j && items[j][0] % items[i][0] == 0) freeCount[i]++;
            }
        }
        vector<int> dp(budget + 1, 0);
        for (int i = 0; i < n; i++) {
            int cost = items[i][1];
            int gain = 1 + freeCount[i];
            for (int b = budget; b >= cost; b--) {
                dp[b] = max(dp[b], dp[b - cost] + gain);
            }
        }
        int ans = 0;
        for (int b = 0; b <= budget; b++) {
            int extra = (budget - b) / minPrice;
            ans = max(ans, dp[b] + extra);
        }
        return ans;
    }
};