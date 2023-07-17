from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_val, max_val = min(nums), max(nums)
        res = 0

        for num in nums:
            if min_val < num < max_val:
                res += 1
        
        return res