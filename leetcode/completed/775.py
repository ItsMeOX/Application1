from typing import List
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        max_ = nums[0]

        for i in range(2, len(nums)):
            max_ = max(max_, nums[i-2])
            if nums[i] < max_:
                return False
            
        return True
        # [3,2,1]
        # [3,4,1]