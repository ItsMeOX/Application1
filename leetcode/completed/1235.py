from typing import List
from functools import lru_cache

# Create a triplet which stores (start, end, profit) for each indices i.
# Then sort the triplet by starting time.
# Starting at i = 0, we can either
# 1. skip current schedule, so search for next schedule which start time >= current start time.
# 2. take current schedule, so profit[i] + next schedule which start time >= current end time.

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        time = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        time.sort()

        def search(target, lo):
            lo, hi = lo, len(time)
            while lo < hi:
                m = (lo+hi) // 2
                if time[m][0] >= target:
                    hi = m
                else:
                    lo = m + 1
            return lo

        @lru_cache(None)
        def dfs(i):
            if i == len(time):
                return 0
            
            # skip
            res = dfs(search(time[i][0], i+1)) # actually can just dfs(i+1) here.

            # take
            res = max(res, time[i][2] + dfs(search(time[i][1], i+1)))

            return res

        return dfs(0)


# Using indices array instead of triplet tuple
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        indices = [i for i in range(len(startTime))]
        indices.sort(key = lambda e: startTime[e])

        def search(target, lo):
            lo, hi = lo, len(indices)
            while lo < hi:
                m = (lo+hi) // 2
                if startTime[indices[m]] >= target:
                    hi = m
                else:
                    lo = m + 1
            return lo

        @lru_cache(None)
        def dfs(i):
            if i == len(indices):
                return 0
            
            # skip
            res = dfs(search(startTime[indices[i]], i+1))

            # take
            res = max(res, profit[indices[i]] + dfs(search(endTime[indices[i]], i+1)))

            return res

        res = 0

        return dfs(0)


#Bottom up approach
from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        indices = [i for i in range(len(startTime))]
        indices.sort(key = lambda e: startTime[e])

        starts = sorted(startTime)

        dp = [0] * (len(indices)+1)

        for i in range(len(indices)-1, -1, -1):
            dp[i] = dp[i+1]
            dp[i] = max(dp[i], profit[indices[i]] + dp[bisect_left(starts, endTime[indices[i]], lo = i+1)])

        return dp[0]