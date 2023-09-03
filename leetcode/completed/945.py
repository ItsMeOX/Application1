from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                res    += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        
        return res


# 1 1 2 2 3 7
# 1 2 2 2 3 7  1
# 1 2 3 2 3 7  1
# 1 2 3 4 3 7  2
# 1 2 3 4 5 7  2 