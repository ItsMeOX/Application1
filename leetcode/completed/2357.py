from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nonzero = 0
        res = 0
        for num in nums:
            if num > 0:
                nonzero += 1

        while nonzero > 0:
            min_ = 100
            for num in nums:
                if num > 0:
                    min_ = min(min_, num)
                    
            for i in range(len(nums)):
                if nums[i] == min_: nonzero -= 1
                nums[i] -= min_
            res += 1

        return res
    

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in set(nums):
            if num > 0:
                res += 1

        return res
    
    
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        seen = set()

        for num in nums:
            if num > 0 and num not in seen:
                seen.add(num)
                res += 1

        return res