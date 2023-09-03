from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            res = 0
            temp = nums[i]
            while temp:
                res = res * 10 + temp % 10
                temp //= 10
            nums.append(res)
        
        return len(set(nums))