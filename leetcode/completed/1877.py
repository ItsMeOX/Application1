from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        len_nums = len(nums)
        res = 0
        for i in range(len_nums // 2):
            res = max(res, nums[i]+nums[len_nums-1-i])
        
        return res