from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            m = (lo + hi) // 2
            if nums[m] < nums[m+1]:
                lo = m + 1
            else:
                hi = m
        
        return lo