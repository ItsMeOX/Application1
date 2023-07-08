from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        cur_longest = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_longest += 1
            else:
                res = max(res, cur_longest)
                cur_longest = 1

        return max(res, cur_longest) 