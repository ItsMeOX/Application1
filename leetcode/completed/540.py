from typing import List

# [1,1,2,3,3,4,4,8,8]
# for index i = even, nums[i] must be == nums[i+1],
# for index i = odds, nums[i] must be == nums[i-1].

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            m = (lo+hi) // 2

            if m & 1:
                if nums[m-1] != nums[m]:
                    hi = m
                else:
                    lo = m + 1
            else:
                if nums[m+1] != nums[m]:
                    hi = m
                else:
                    lo = m + 1
        
        return nums[lo]