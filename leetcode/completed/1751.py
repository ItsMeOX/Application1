from typing import List
from bisect import bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        start = [events[i][0] for i in range(len(events))]
        memo = {}

        def dfs(i, attended):
            if attended == k or i == len(events):
                return 0

            if (i, attended) in memo:
                return memo[(i, attended)]

            next_idx = bisect_right(start, events[i][1])
            res = max(dfs(i+1, attended), events[i][2] + dfs(next_idx, attended+1))

            memo[(i, attended)] = res
            return res


        return dfs(0, 0)