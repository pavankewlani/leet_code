class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int> pd;
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                pd.push(matrix[i][j]);
                if(pd.size()>k){
                    pd.pop();
                }
            }
        }
        int ans=pd.top();
        return ans;
    }
};