from typing import List
from functools import cache

# Calculate the intervals of every taps and sort them by their starting point.
# We start at every taps that starts before x <= 0,
# then for every taps, we will traverse the next taps which
# the starting point of next tap is <= ending point of this tap.
# If we reach a tap that ending point >= n, return 0.

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        intervals = []
        for i in range(len(ranges)):
            intervals.append((i-ranges[i], i+ranges[i]))
        intervals.sort()

        @cache
        def dfs(i):
            if intervals[i][1] >= n:
                return 0
            
            res = float('inf')
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= intervals[i][1]:
                    res = min(res, dfs(j) + 1)
                else:
                    break

            return res
        
        res = float('inf')
        for i in range(len(intervals)):
            s, e = intervals[i]
            if s <= 0:
                res = min(res, dfs(i) + 1)
            else:
                break
        
        return res if res < float('inf') else -1
    

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(len(ranges)):
            intervals.append((i-ranges[i], i+ranges[i]))
        intervals.sort()

        dp = [float('inf')] * (n+1)
        dp[-1] = 0

        for i in range(n-1, -1 ,-1):
            if intervals[i][1] >= n:
                dp[i] = 0
                continue
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= intervals[i][1]:
                    dp[i] = min(dp[i], dp[j]+1)
                else:
                    break
        
        res = float('inf')
        for i in range(len(intervals)):
            s, e = intervals[i]
            if s <= 0:
                res = min(res, dp[i] + 1)
            else:
                break

        return res if res < float('inf') else -1

# Can be solved using greedy at O(n).
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_distance = [0] * (n+1)

        for i in range(len(ranges)):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])

            max_distance[start] = max(max_distance[start], end)

        cur_end , next_end, res = 0, 0, 0

        for i in range(n+1):
            if i > next_end:
                return -1

            if i > cur_end:
                res += 1
                cur_end = next_end
            
            next_end = max(next_end, max_distance[i])

        return res