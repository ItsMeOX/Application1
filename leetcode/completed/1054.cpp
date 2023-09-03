#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        unordered_map<int, int> map;
        priority_queue<pair<int, int>> heap;

        for (auto bar : barcodes) map[bar]++;

        for (auto key : map) heap.push({key.second, key.first});

        vector<int> res(barcodes.size());
        int i = 0;

        while (!heap.empty()) {
            pair<int, int> pair = heap.top();
            heap.pop();
            int count = pair.first, num = pair.second;

            while (count-- > 0) {
                if (i >= barcodes.size()) i = 1;
                res[i] = num;
                i += 2;
            }
        }

        return res;

    }
};