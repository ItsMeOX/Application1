from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        if n & 1:
            median = nums[n//2]
        else:
            median = (nums[n//2 - 1] + nums[n//2]) // 2

        res = 0

        for i in range(n):
            res += abs(nums[i] - median)

        return res