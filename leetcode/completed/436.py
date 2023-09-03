from typing import List
from bisect import bisect_left

# For each end at index i, 
# binary search for index j such that start_j >= end.

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([intervals[i][0] for i in range(len(intervals))])
        indices = {intervals[i][0]: i for i in range(len(intervals))}
        res = [-1] * len(intervals)

        for i in range(len(intervals)):
            _, end = intervals[i]
            starts_index = bisect_left(starts, end)
            if starts_index == len(starts):
                continue
            res[i] = indices[starts[starts_index]]

        return res