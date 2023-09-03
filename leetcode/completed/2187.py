from typing import List

# Maybe maybe maybe if we see a 'list' and a 'k', we can think of using binary search.
# We set lower bound to 1, upper bound to minimum time * totalTrips (as it takes as most min_time * totalTrips to complete totalTrips.)
# Every iteration of binary search, we loop through 'time' array, and count how many trips we can achieve with 'm' days for each bus and sum it up.
# If the n. of trips <  totalTrips, then we need more days, so set lower bound to m+1.
# If the n. of trips >= totalTrips, then we might be able to achieve n. of totalTrips with lesser days, so we set higher bound to m.
# At the end of iteration of binary search, lo will equal to hi and it will be our answer.

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 1, min(time)*totalTrips

        def check(num):
            res = 0
            for t in time:
                res += num // t
            return res
        
        while lo < hi:
            m = (lo+hi) // 2
            if check(m) < totalTrips:
                lo = m + 1
            else:
                hi = m
        
        return lo