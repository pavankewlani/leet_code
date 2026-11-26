class Solution {
public:
    bool canAliceWin(int n) {
        int temp = n;
        int take = 10;
        bool alice = true;
        while (temp >= take) {
            temp -= take;
            take--;
            alice = !alice;
        }
        return !alice;
    }
};