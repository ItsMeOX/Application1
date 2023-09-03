#include <string>

using namespace std;

class Solution {
public:
    int partitionString(string s) {
        char seen[256] = {};
        int res = 1;

        for (const auto& c : s) {
            if (seen[c]++ == 1) {
                res++;
                memset(seen, 0, 256);
                seen[c]++;
            }
        }

        return res;

    }
};