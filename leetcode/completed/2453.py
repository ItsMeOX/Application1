from typing import List
from collections import defaultdict

# Observation:
# Any series numbers added by k will always have the same remainder if % by k.
# y = 2*x + 1
# series: 1, 3, 5, 7, 9...
# every numbers % 2 = 1.

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        counter = defaultdict(int)

        for num in nums:
            counter[num % space] += 1
        
        max_val = max(counter.values())

        res = nums[0]
        for num in nums:
            if counter[num % space] > counter[res % space]:
                res = num
            elif counter[num % space] == counter[res % space] and num < res:
                res = num
        
        return res