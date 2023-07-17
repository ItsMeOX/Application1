from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        count = defaultdict(int)

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                if product in count:
                    res += 8 * count[product]
                count[product] += 1

        return res