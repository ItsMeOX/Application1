#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int m = grid.size(), n = grid[0].size();
        vector<int> flatten;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                flatten.push_back(grid[i][j]);
            }
        }
        sort(flatten.begin(), flatten.end());

        int target = flatten[flatten.size()/2];

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (abs(grid[i][j]-target) % x > 0) return -1;
                res += abs(grid[i][j]-target) / x;
            }
        }

        return res;

    }
};