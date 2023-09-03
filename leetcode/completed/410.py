from typing import List

# Perform a binary search where m = maximum subarray sum.
# Lower bound cannot be 0, and should be max(nums) because for example:
# [1,4,4], k=3
# 4 -> requires 3, 
# 1 -> also requires 3, so we should limit lower bound to max(nums).
# Higher bound will be when k = 1, and the sum of subarray will be sum of whole array.
# If subs_needed to cover whole array and sums(subarray) <= m is
# <= k: that means that the capacity is too large, so we should lower it,
# >  k: that means that the capacity is too small and we need more than k subarrays to cover whole array.

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        lo, hi = max(nums), sum(nums)

        while lo < hi:
            m = (lo+hi) // 2

            subs_needed = 1
            sums = 0
            for num in nums:
                if sums + num > m:
                    sums = 0
                    subs_needed += 1
                sums += num
            
            if subs_needed <= k:
                hi = m
            else:
                lo = m + 1
        
        return lo