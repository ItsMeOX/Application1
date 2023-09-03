#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> res(n-2, vector<int>(n-2, 0));
        for (int r = 1; r < n-1; r++) {
            for (int c = 1; c < n-1; c++) {
                int t = 0;
                for (int dr = -1; dr < 2; dr++) {
                    for (int dc = -1; dc < 2; dc++) {
                        t = max(t, grid[r+dr][c+dc]);
                    }
                }
                res[r-1][c-1] = t;
            }
        }

        return res;
    }
};