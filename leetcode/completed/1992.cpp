#include <vector>
#include <deque>
#include <utility>

using namespace std;

class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        deque<pair<int, int>> q;
        int m = land.size(), n = land[0].size();
        vector<vector<int>> directions{{0, 1}, {1, 0}};
        vector<vector<int>> res;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (land[r][c] == 1) {
                    land[r][c] = -1;
                    vector<int> rect{r, c, 0, 0};
                    q.push_back(make_pair(r, c));
                    while (!q.empty()) {
                        int rr = q.front().first;
                        int cc = q.front().second;
                        q.pop_front();
                        rect[2] = rr;
                        rect[3] = cc;
                        for (const auto& direction : directions) {
                            int dr = direction[0], dc = direction[1];
                            if (rr+dr < m && cc+dc < n && land[rr+dr][cc+dc] == 1) {
                                land[rr+dr][cc+dc] = -1;
                                q.push_back(make_pair(rr+dr, cc+dc));
                            }
                        }
                    }
                    res.push_back(rect);
                }
            }
        }
        return res;
    }
};