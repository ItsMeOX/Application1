#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int res = 0;
        int edge = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        vector<int> visited(points.size(), 0);
        heap.push({0, 0});

        while (edge < points.size()) {
            const pair<int, int>& elm = heap.top();
            int cost = elm.first;
            int i = elm.second;
            heap.pop();

            if (visited[i] == 1) continue;
            visited[i] = 1;
            res += cost;
            edge++;

            for (int j = 0; j < points.size(); j++) {
                if (visited[j] == 0) {
                    int new_cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                    heap.push({new_cost, j});
                }
            }
        }

        return res;

    }
};