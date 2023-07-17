from typing import List
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        ranges = defaultdict(list)

        for i, num in enumerate(nums):
            ranges[num].append(i)
        keys = sorted(ranges.keys())

        for left, right in queries:
            prev, temp = 0, float('inf')
            for key in keys:
                idx = bisect_left(ranges[key], left)
                if idx != len(ranges[key]) and ranges[key][idx] <= right:
                    if prev:
                        temp = min(temp, key-prev)
                    prev = key
            if temp != float('inf'):
                res.append(temp)
            else:
                res.append(-1)
        
        return res