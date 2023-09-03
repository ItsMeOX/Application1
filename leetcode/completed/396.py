from typing import List

# For example: [4, 3, 2, 6]
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 16
# from F(0) to F(1), 25 - 3(6) + (4+3+2) = 16
# we can deduce that f(n-1) - (len-1)*(arr[-n]) + (sum(arr)-arr[-n]) = f(n).


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sums = sum(nums)
        prev = 0

        for i in range(len(nums)):
            prev += nums[i] * i
        
        res = prev
        cur = 0

        for i in range(1, len(nums)):
            cur = prev - (len(nums)-1)*(nums[-i]) + (sums - nums[-i])
            prev = cur
            res = max(res, cur)

        return res
