from math import ceil
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        lo, hi = 1, 10 ** 7
        if ceil(hour) < len(dist): return -1

        while lo < hi:
            m = (lo+hi) // 2
            time_needed = 0
            for i in range(len(dist)-1):
                time_needed += ceil( dist[i] / m )
            time_needed += ( dist[-1] / m )
            if time_needed <= hour:
                hi = m
            else:
                lo = m + 1
        
        return lo