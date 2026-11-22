class Solution {
public:
    bool checkString(string s) {

        for(int i=0;i<s.size()-1;i++){
            if((s[i]=='b' && s[i+1]=='a')||(s[i]=='B' && s[i+1]=='A')){
                return false;
            }
        }
        return true;
    }
};