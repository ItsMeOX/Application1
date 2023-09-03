#include <vector>

using namespace std;

class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        bool seen [101] = {false};
        int pair = 0;

        for (auto num : nums) {
            pair = seen[num] == true ? pair + 1 : pair;
            seen[num] = !seen[num];
        }

        vector<int> res = {pair, (int)nums.size() - pair*2};

        return res;

    }
};