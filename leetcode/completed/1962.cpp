#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int>pq;

        for (int p : piles) {
            pq.push(p);
        }

        for (; k > 0; k--) {
            int temp = pq.top();
            pq.pop();
            temp -= temp / 2;
            pq.push(temp);
        }

        int res = 0;
        while (!pq.empty()) {
            res += pq.top();
            pq.pop();
        }

        return res;

    }
};