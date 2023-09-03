from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for num in nums:
            if abs(num) < abs(res): # if num is closer to 0 than res, update res to num.
                res = num
            if abs(res) == num: # for example num = 1, res = -1, then update res to num.
                res = num

        return res