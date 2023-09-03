from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        res = 0
        for key in counter:
            if key+1 in counter:
                res = max(res, counter[key]+counter[key+1])
        
        # can one pass if also check for key-1 while iterating through the nums.

        return res