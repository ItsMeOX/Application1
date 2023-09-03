from typing import List

# Sort the intervals by starting time.
# Append the first interval in intervals to a list('res').
# From the second interval, check if the starting time of the interval is more late than the last interval in 'res'.
# If yes, then there is not overlapping between two intervals, so just append the interval to 'res'.
# If not, then we merge two intervals by update the ending of last interval in 'res' to the latest time.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            elif end > res[-1][1]:
                res[-1][-1] = end

        return res