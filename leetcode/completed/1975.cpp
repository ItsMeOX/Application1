#include <vector>
#include <algorithm>

using namespace std;

// 

class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long res = 0;
        int m = matrix.size(), n = matrix[0].size();
        int neg_cnt = 0;
        int min_val = INT_MAX;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                res += abs(matrix[r][c]);
                neg_cnt += (matrix[r][c] <= 0);
                min_val = min(min_val, abs(matrix[r][c]));
            }
        }

        return neg_cnt & 1 == 1 ? res - min_val*2 : res;

    }
};