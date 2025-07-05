class Solution {
public:
    int singleNumber(vector<int>& li) {
        bool isFound = true;
        int ind = 0;
        int res = 0;
        
        for (int i = 0; i < li.size(); i++) {
            res = li[i];
            for (int j = 0; j < li.size(); j++) {
                if (i != j && li[i] == li[j]) {
                    isFound = true;
                    break;
                } else {
                    isFound = false;
                }
            }
            if (isFound == false) {
                break;
            }
        }

        return res;
    }
};
