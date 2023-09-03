from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        max_val = 0
        prefix = 0
        res = []

        for num in nums:
            max_val = max(max_val, num)
            prefix += max_val + num
            res.append(prefix)

        return res