class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int n = heights.size();
        int maxi = 0;

        for(int i = 0; i <= n; i++){
            int curr;
            if(i == n) curr = 0;
            else curr = heights[i];
            while(!st.empty() && heights[st.top()] > curr)
            {
                int h = heights[st.top()];
                st.pop();
                int width;
                if(st.empty()) width = i;
                else width = i - st.top() - 1;
                int area = h * width;
                maxi = max(maxi, area);
            }
            st.push(i);
        }
        return maxi;
    }
};